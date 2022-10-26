r"""Simple AES encryption example leveraging pyCryptodome.

 ______                         __ _______ __         __ __
|      |.----.-----.--.--.--.--|  |     __|  |_.----.|__|  |--.-----.
|   ---||   _|  _  |  |  |  |  _  |__     |   _|   _||  |    <|  -__|
|______||__| |_____|________|_____|_______|____|__|  |__|__|__|_____|

     **      ********  ********
    ****    /**/////  **//////
   **//**   /**      /**
  **  //**  /******* /*********
 ********** /**////  ////////**
/**//////** /**             /**     Simple encryption example #3
/**     /** /******** ********
//      //  //////// ////////

This solution leverages pyCryptodome to AES encrypt API credentials
to a static file. This file is then consumed in follow up executions
of the tool to acquire the API credentials used to demonstrate that
connectivity to the CrowdStrike API is functional.

This tool can also be used to AES/CBC encrypt and decrypt regular text.

REQUIRES
    click                   https://click.palletsprojects.com/en/8.1.x/
    crowdstrike-falconpy    https://github.com/CrowdStrike/falconpy
    pycryptodomex           https://snyk.io/advisor/python/pycryptodome

RUNNING THE API CONNECTIVITY DEMONSTRATION
Step 1) Generate an encrypted credential file using the `--g` (--generate) argument.
Step 2) Execute the program again, passing the name of your newly created
        encrypted credential file using the `-f` argument.
Step 3) Provide the secret key you created in Step 1 when prompted.
        Note: You can provide this on the command line with the `-k` argument.
Step 4) Review API results.

ENCRYPTING / DECRYPTING TEXT
These operations do not make use of your encrypted credential file.
Step 1) Use the `-e` (--encrypt) and `-d` (--decrypt) arguments to specify the
        operation you wish to perform. If you do not provide a key with the `-k`
        argument, you will be asked to provide one. If you do not provide plain
        or cipher text using the `-t` argument, you will be ask to supply it.
Step 2) Review cryptographic results.
"""
# pylint: disable=E0401,E0611,E1003
from argparse import ArgumentParser, RawTextHelpFormatter, Namespace, SUPPRESS
from base64 import b64encode, b64decode
from hashlib import sha256
from os.path import exists
from sys import exit as end_of_line
from json import dumps, loads
from click import prompt
from Cryptodome import Random
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
from falconpy import Hosts


class AESCrypt:
    """Wrapper class for the functionality provided by pyCryptodome."""

    class InvalidKeySpecified(Exception):
        """Class specific custom error handling for when a key is not specified."""

        def __init__(self, *args, message: str = "The string '{}' is not a valid key."):
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


def consume_key_file(key_file: str, key_str: str):
    """Consume the key file and retrieve the key."""
    if not exists(key_file):
        raise SystemExit("  ⛔ Specified key file does not exist")
    try:
        crypt = AESCrypt(key=key_str)
    except (
            AESCrypt.InvalidKeySpecified,
            AESCrypt.KeyTooSmall,
            AESCrypt.EmptyKeySpecified,
            AESCrypt.WrongKeyFormat
            ) as bad_key:
        raise SystemExit("  ⛔ Invalid secret key provided for this encryption.") from bad_key
    with open(key_file, "rb") as reading:
        try:
            returned = crypt.decrypt(b64decode(reading.read()).decode())
        except AESCrypt.InvalidSecret as bad_secret:
            raise SystemExit(
                "  ⛔ Invalid secret key provided for this encryption."
                ) from bad_secret

    return returned


def consume_arguments():
    """Consume any provided command line arguments."""
    parser = ArgumentParser(description=__doc__,
                            formatter_class=RawTextHelpFormatter,
                            argument_default=SUPPRESS
                            )
    parser.add_argument("-t", "--text", help="Text to encrypt or decrypt", default=None)
    parser.add_argument("-k", "--key", help="Key to use for encryption operations", default=None)
    parser.add_argument("-f", "--keyfile",
                        help="File to save your encrypted credentials too",
                        default=None
                        )
    parser.add_argument("-g", "--generate",
                        help="Generate a new keyfile using a key you specify",
                        action="store_true",
                        default=False
                        )
    wot = parser.add_mutually_exclusive_group(required=False)
    wot.add_argument("-d", "--decrypt",
                     help="Decrypt the provided string",
                     action="store_true",
                     default=False
                     )
    wot.add_argument("-e", "--encrypt",
                     help="Encrypt the provided string",
                     action="store_true",
                     default=False
                     )

    return parser.parse_args()


def perform_api_example(creds: dict):
    """Perform a CrowdStrike API connectivity test.

    This test will connect to the Hosts API using the credentials stored in the encrypted
    credential file, and then pull the hostnames and device IDs for every host within the tenant.
    """
    # Number of records per query
    data_batch_size = 5000

    # Demonstrate API access using the encrypted credentials
    hosts = Hosts(**creds)
    if hosts.token_status != 201:
        raise SystemExit(
            "  ⚠️  Unable to authenticate with the CrowdStrike API using the credentials provided."
            )
    total = 1
    offset = None
    host_list = []
    req_count = 0
    while len(host_list) < total:
        req_count += 1
        print(f"  ⬇️  Retrieving host IDs from the CrowdStrike API (request #{req_count}),"
              " please wait...",
              end="\r",
              flush=True
              )
        host_lookup = hosts.query_devices_by_filter_scroll(limit=data_batch_size, offset=offset)
        offset = host_lookup["body"]["meta"]["pagination"]["offset"]
        total = host_lookup["body"]["meta"]["pagination"]["total"]
        if host_lookup["body"]["resources"]:
            host_list.extend(host_lookup["body"]["resources"])
    print(
        f"\n  ✅ ID retrieval of {len(host_list)} hosts completed, requesting extended host details"
        )
    host_details = []
    host_batches = [
        host_list[i:i+data_batch_size] for i in range(0, len(host_list), data_batch_size)
        ]
    rec_pos = 0
    for batch in host_batches:

        print(f"  ⬇️  Downloading host detail from the CrowdStrike API for records {rec_pos} "
              f"to {len(batch)+rec_pos} of {len(host_list)} hosts, please wait...",
              end="\r",
              flush=True
              )
        rec_pos += len(batch)
        host_detail_lookup = hosts.get_device_details(batch)
        host_details.extend(host_detail_lookup["body"]["resources"])
    print("\n  ✅ Host detail retrieval complete, showing results.")
    for host in host_details:
        print(f"  🖥  {host.get('hostname', 'Not found'):<50} [{host['device_id']}]")

    print("\n  ✅ All done!")


def get_key(cmd_line: Namespace):
    """Request the user provide their current secret key."""
    if not cmd_line.key:
        cmd_line.key = prompt("  ❓ Please provide your secret key ", hide_input=True)

    return cmd_line.key


def get_cred_file(cmd_line: Namespace, check_exists: bool = True):
    """Request the user provide their credential file name."""
    keyfile = cmd_line.keyfile
    stub = "used to store"
    if not check_exists:
        stub = "to use for storing"
    if not keyfile:
        keyfile = prompt(
            f"  ❓ Please specify the file {stub} your encrypted credentials: "
            )
    if not exists(keyfile) and check_exists:
        raise SystemExit(f"  📛 The specified key file, {keyfile} does not exist.")

    return keyfile


def get_cryptor(cmd_line: Namespace, fail_on_error: bool = True):
    """Return an instance of the AESCrypt class handling invalid keys gracefully."""
    cryptor = None
    try:
        cryptor = AESCrypt(cmd_line.key)
    except (
        AESCrypt.InvalidKeySpecified,
        AESCrypt.EmptyKeySpecified,
        AESCrypt.WrongKeyFormat,
        AESCrypt.KeyTooSmall
    ) as encrypt_fail:
        if fail_on_error:
            raise SystemExit(f"  🚫 {encrypt_fail.message}") from encrypt_fail

        print(f"  🚫 {encrypt_fail.message}")

    return cryptor


def set_crowdstrike_credentials():
    """Ask the user for the CrowdStrike API credentials to encrypt."""
    id_val = prompt("  ❓ Please provide your CrowdStrike API Client ID ", hide_input=True)
    sec_val = prompt("  ❓ Please provide your CrowdStrike API Client Secret ",
                     hide_input=True
                     )
    if not id_val and not sec_val:
        raise SystemExit(
            "  ❌ You must provide these values in order to generate an encrypted credential file."
            )

    return id_val, sec_val


def get_text_to_handle(cmd_line: Namespace, method: str = "encrypt"):
    """Ask the user to provide the cipher or plain text to be handled."""
    text_to_handle = cmd_line.text
    if not text_to_handle:
        text_to_handle = prompt(f"  ❓ What text would you like me to {method}? ")

    return text_to_handle


def do_simple_decrypt(cmd_line: Namespace):
    """Decrypt the provided plain text and exit."""
    cmd_line.key = get_key(cmd_line)
    decryptor: AESCrypt = get_cryptor(cmd_line)
    cmd_line.text = get_text_to_handle(cmd_line, "decrypt")
    try:
        print(f"  🔓 Decrypted: {decryptor.decrypt(cmd_line.text)}")
    except AESCrypt.InvalidSecret as bad_key:
        raise SystemExit("  ⛔ Invalid secret key provided for this encryption.") from bad_key
    end_of_line(0)


def do_simple_encrypt(cmd_line: Namespace):
    """Encrypt the provided cipher text and exit."""
    cmd_line.key = get_key(cmd_line)
    encryptor: AESCrypt = get_cryptor(cmd_line)
    cmd_line.text = get_text_to_handle(cmd_line)
    print(f"  🔐 Encrypted: {encryptor.encrypt(cmd_line.text)}")
    end_of_line(0)


def ask_for_valid_key(cmd_line: Namespace):
    """Hold the user in a loop until they provide a valid secret key."""
    success = False
    while not success:
        # Stay in the loop until they give us a valid key
        cmd_line.key = get_key(cmd_line)
        crypt_obj = get_cryptor(cmd_line, fail_on_error=False)
        if not crypt_obj:
            cmd_line.key = None
        else:
            success = True

    return crypt_obj


def generate_encrypted_credential_file(cmd_line: Namespace, c_id: str, c_sec: str):
    """Create the AESCrypt object and encrypt the credentials dictionary to a file."""
    crypt = ask_for_valid_key(cmd_line)
    creds = {"client_id": c_id, "client_secret": c_sec}
    with open(cmd_line.keyfile, "wb") as encrypted_file:
        encrypted_file.write(b64encode(crypt.encrypt(dumps(creds)).encode()))


if __name__ == "__main__":
    # Retrieve any provided command line arguments
    cmdline = consume_arguments()
    if cmdline.generate:
        # ____ _  _ ____ ____ _   _ ___  ___
        # |___ |\ | |    |__/  \_/  |__]  |
        # |___ | \| |___ |  \   |   |     |
        # ____ ____ ____ ___  ____ _  _ ___ _ ____ _    ____
        # |    |__/ |___ |  \ |___ |\ |  |  | |__| |    [__
        # |___ |  \ |___ |__/ |___ | \|  |  | |  | |___ ___]
        # Ask the user for their API client ID and secret
        client_id, client_secret = set_crowdstrike_credentials()
        # Ask the user for the name of the new credential file
        cmdline.keyfile = get_cred_file(cmdline, check_exists=False)
        # Encrypt our credential dictionary and write it to the credential file
        generate_encrypted_credential_file(cmdline, client_id, client_secret)
    else:
        if cmdline.decrypt:
            # ___  ____ ____ ____ _   _ ___  ___    ___ ____ _  _ ___
            # |  \ |___ |    |__/  \_/  |__]  |      |  |___  \/   |
            # |__/ |___ |___ |  \   |   |     |      |  |___ _/\_  |
            # Perform a simple decryption operation
            do_simple_decrypt(cmdline)
        if cmdline.encrypt:
            # ____ _  _ ____ ____ _   _ ___  ___    ___ ____ _  _ ___
            # |___ |\ | |    |__/  \_/  |__]  |      |  |___  \/   |
            # |___ | \| |___ |  \   |   |     |      |  |___ _/\_  |
            # Perform a simple encryption operation
            do_simple_encrypt(cmdline)

        # Retrieve the encrypted credential file
        cmdline.keyfile = get_cred_file(cmdline)
        # Retrieve the secret key
        cmdline.key = get_key(cmdline)
        # Decrypt and consume the encrypted file and retrieve the API credentials
        credentials = loads(consume_key_file(cmdline.keyfile, cmdline.key))
        # _  _ ____ ____    ____ _  _ ____ ____ _   _ ___  ___ ____ ___
        # |  | [__  |___    |___ |\ | |    |__/  \_/  |__]  |  |___ |  \
        # |__| ___] |___    |___ | \| |___ |  \   |   |     |  |___ |__/
        # ____ ____ ____ ___  ____ _  _ ___ _ ____ _    ____
        # |    |__/ |___ |  \ |___ |\ |  |  | |__| |    [__
        # |___ |  \ |___ |__/ |___ | \|  |  | |  | |___ ___]
        # We have everything we need, perform
        # a demonstration using the Hosts API
        perform_api_example(credentials)
