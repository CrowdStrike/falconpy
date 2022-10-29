r"""Encrypt or decrypt a file with AES256/CBC encryption.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |                         |::.. . |
`-------'                         `-------'

     _______ _______ _______      ___  ______ ______ ______
    |   _   |    ___|     __|    /  / |      |   __ \      |
    |       |    ___|__     |  ,' ,'  |   ---|   __ <   ---|
    |___|___|_______|_______| /__/    |______|______/______|

             _______ __ __           ______                    __
            |    ___|__|  |.-----.  |      |.----.--.--.-----.|  |_
            |    ___|  |  ||  -__|  |   ---||   _|  |  |  _  ||   _|
            |___|   |__|__||_____|  |______||__| |___  |   __||____|
                                                 |_____|__|

Chunks read and write operations to handle larger file sizes.
"""
# pylint: disable=E0401,E0611,E1003
from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from hashlib import sha256, md5
from base64 import b64decode, b64encode
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding


class AESCrypt:
    """Wrapper class for the functionality provided by pyCryptodome."""

    class InvalidKeySpecified(Exception):
        """Class specific custom error handling for when a key us not specified."""

        def __init__(self, *args, message: str = "The provided string is not a valid key."):
            """Initialize an instance of the exception."""
            self.message = message
            super().__init__(self.message, *args)

    class KeyTooSmall(InvalidKeySpecified):
        """Class specific custom error handling for keys that have too short of a length."""

        def __init__(self,
                     *args,
                     key: str,
                     message: str = "The key '{}' is too small (must be > 8 characters).",
                     ):
            """Initialize an instance of the exception."""
            self.key = key
            self.message = message.format(self.key)
            super(AESCrypt.InvalidKeySpecified, self).__init__(self.message, *args)

    class EmptyKeySpecified(InvalidKeySpecified):
        """Class specific custom error handling for empty keys."""

        def __init__(self, *args, key: str = None, message: str = "The key cannot be empty."):
            """Initialize an instance of the exception."""
            self.key = key
            self.message = message
            super(AESCrypt.InvalidKeySpecified, self).__init__(self.message, *args)

    class WrongKeyFormat(InvalidKeySpecified):
        """Class specific custom error handling for keys that are using the wrong format."""

        def __init__(self,
                     *args,
                     key: str = None,
                     message: str = "The provided key utilizes the "
                     "wrong text encoding or format (not UTF-8)."
                     ):
            """Initialize an instance of the exception."""
            self.key = key
            self.message = message
            super(AESCrypt.InvalidKeySpecified, self).__init__(self.message, *args)

    class InvalidSecret(InvalidKeySpecified):
        """Class specific custom error handling for keys that are incorrect."""

        def __init__(self,
                     *args,
                     key: str = None,
                     message: str = "The provided key is not correct.",
                     ):
            """Initialize an instance of the exception."""
            self.key = key
            self.message = message
            super(AESCrypt.InvalidKeySpecified, self).__init__(self.message, *args)

    __BLOCK_SIZE__ = 16

    def __init__(self, key: str = None):
        """Initialize an instance of the AESCrypt class."""
        if key.strip() == "":
            raise self.EmptyKeySpecified
        if not isinstance(key, str):
            raise self.WrongKeyFormat
        if not len(key) > 8:
            raise self.KeyTooSmall(key=key)

        self.key = self.gen_key(key_str=key)

    @staticmethod
    def gen_key(key_str: str = None):
        """Generate a properly padded AES CBC key."""
        if not key_str:
            key_str = "FungoBat!"
        if not isinstance(key_str, bytes):
            key_str = key_str.encode()

        return sha256(key_str).digest()

    def encrypt(self, raw):
        """Encode the provided plaintext using the provided key."""
        raw = bytes(Padding.pad(data_to_pad=raw.encode('utf-8'), block_size=self.__BLOCK_SIZE__))
        init_vector = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, init_vector)

        return b64encode(init_vector + cipher.encrypt(raw)).decode('utf-8')

    def decrypt(self, enc):
        """Decode the provided ciphertext using the provided key."""
        enc = b64decode(enc)
        init_vector = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, init_vector)
        try:
            decoded = Padding.unpad(
                padded_data=cipher.decrypt(enc[AES.block_size:]),
                block_size=self.__BLOCK_SIZE__)
        except ValueError as bad_key:
            raise self.InvalidSecret from bad_key

        return decoded.decode()


def hash_file(source_file: str, buf_size: int):
    """Run MD5 and SHA256 hashes on the file specified and return the result."""
    md5_hash = md5()  # nosec  # Not used for cryptographic operations, False Positive
    sha_hash = sha256()

    with open(source_file, 'rb') as file_of_interest:
        while True:
            data = file_of_interest.read(buf_size)
            if not data:
                break
            md5_hash.update(data)
            sha_hash.update(data)

    return md5_hash, sha_hash


def cryptor(key: str):
    """Return an instance of the AESCrypt class."""
    return AESCrypt(key)


def encrypt_file(source_file: str, target_file: str, magic_word: str, buf_size: int):
    """Encrypt the specified source file to the target file using the provided key."""
    enc_str = []
    crypt = cryptor(magic_word)
    with open(source_file, "rb") as source:
        while True:
            data = source.read(buf_size)
            if not data:
                break
            enc_str.append(crypt.encrypt(data.decode()))

    encoded = "".join(enc_str).encode()

    with open(target_file, "wb") as target:
        for part in [encoded[i:i+buf_size] for i in range(0, len(encoded), buf_size)]:
            target.write(part)

    print(f"  🔐 Completed encryption of {source_file} to {target_file}.")


def decrypt_file(enc_file: str, target_file: str, magic_word: str, buf_size: int):
    """Decrypt the specified source file to the target file using the provded key."""
    dec_str = []
    crypt = cryptor(magic_word)
    with open(enc_file, "rb", buffering=buf_size) as new_source:
        while True:
            data = new_source.read(buf_size)
            if not data:
                break
            try:
                dec_str.append(crypt.decrypt(data.decode()))
            except AESCrypt.InvalidSecret as bad:
                raise SystemExit("  ⛔ Invalid secret specified for the encryption used.") from bad

    with open(target_file, "w", encoding="utf-8") as decrypted:
        decrypted.write("".join(dec_str))

    print(f"  🔓 Completed decryption of {enc_file} to {target_file}.")


def show_hashes(file_to_hash: str, buffer: int):
    """Hash the specified file and print the results."""
    mdhash, shahash = hash_file(file_to_hash, buffer)
    print(f"  #️⃣     MD5: {mdhash.hexdigest()}")
    print(f"  #️⃣  SHA256: {shahash.hexdigest()}")


def consume_arguments():
    """Parse the provided command line."""
    parser = ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
    option = parser.add_argument_group("behavior arguments")
    requir = parser.add_argument_group("required arguments")
    requir.add_argument("-k", "--key",
                        help="Key to use for encryption and decryption operations.",
                        required=True
                        )
    option.add_argument("-c", "--checksum",
                        help="Print the hash of the target and source file arguments.",
                        required=False,
                        action="store_true",
                        default=False
                        )
    option.add_argument("-d", "--decrypt",
                        help="Decrypt from the source to the target.",
                        required=False,
                        action="store_true",
                        default=False
                        )
    option.add_argument("-e", "--encrypt",
                        help="Encrypt from the source to the target.",
                        required=False,
                        action="store_true",
                        default=False
                        )
    files = parser.add_argument_group("file arguments")
    files.add_argument("-s", "--source", help="Source file to encrypt or decrypt.", required=False)
    files.add_argument("-t", "--target",
                       help="Target file for the resulting cryptographic operation.",
                       required=False
                       )
    parser.add_argument("-b", "--buffer",
                        help="Max buffer size before the contents are written to the target file.",
                        default=65536,
                        required=False,
                        )

    parsed: Namespace = parser.parse_args()
    try:
        parsed.buffer = int(parsed.buffer)
    except ValueError:
        parsed.buffer = 65536

    if parsed.buffer < 32:
        raise SystemExit("  ⛔ Invalid buffer size specified (must be >= 32).")

    return parsed


if __name__ == "__main__":
    # Retrieve the command line
    cmdline = consume_arguments()

    if cmdline.encrypt:
        if cmdline.checksum:
            # Hash the file for integrity checking if asked
            show_hashes(cmdline.source, cmdline.buffer)
        # Encryption requested
        encrypt_file(cmdline.source, cmdline.target, cmdline.key, cmdline.buffer)

    if cmdline.decrypt:
        # Decryption requested
        decrypt_file(cmdline.source, cmdline.target, cmdline.key, cmdline.buffer)
        if cmdline.checksum:
            # Hash the result decrypted file for integrity checking
            show_hashes(cmdline.target, cmdline.buffer)
