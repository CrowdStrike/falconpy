![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo.png#gh-light-mode-only)
![CrowdStrike FalconPy](https://raw.githubusercontent.com/CrowdStrike/falconpy/main/docs/asset/cs-logo-red.png#gh-dark-mode-only)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)

# Authentication examples
The examples in this folder focus on authentication to CrowdStrike's APIs.

- [Azure Key Vault Authentication](#azure-key-vault-authentication) - CrowdStrike API authentication leveraging Azure Key Vault for credential storage.
- [AES Authentication](#aes-authentication) - Leverage AES/CBC to encrypt credentials for use with authentication to the CrowdStrike API.
- [AES File Crypt](#aes-file-crypt) - Encrypt arbitrary files with AES/CBC
- [AWS Parameter Store](#aws-parameter-store) - CrowdStrike API authentication leveraging AWS Parameter Store for credential storage
- [Token Authentication](#token-authentication) - Token Authentication is the original solution for authenticating to a Service Class, and is still fully supported. This example demonstrates how to use Token Authentication to interact with multiple Service Classes.

## Azure Key Vault Authentication
This application demonstrates storing CrowdStrike API credentials within the
Azure Key Vault service, and retrieving them to access the CrowdStrike API.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |

You will also need to ensure you have the following:
1. An Azure Key Vault `https://docs.microsoft.com/azure/key-vault/quick-create-cli`
    > :exclamation: Make note of the **Vault URI** :exclamation:</br>
    > You will use this as a command line argument.
2. Secrets created for your *Falcon Client ID* and *Client Secret*
3. `azure-keyvault-secrets` and `azure-identity` libraries
    ```shell
    pip install azure-keyvault-secrets azure-identity
    ```
4. Set up your environment to use azure-identity's DefaultAzureCredential.
    > For more information about how to configure
    > the DefaultAzureCredential, refer to https://aka.ms/azsdk/python/identity/docs#azure.identity.DefaultAzureCredential

#### Command line arguments
This program accepts the following command line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | Display command line help and exit |
|  `-k` _CLIENT_ID_PARAMETER_ | `--client_id_parameter` _CLIENT_ID_PARAMETER_ | Name of the Key Vault Secrets parameter storing your API client ID |
|  `-s` _CLIENT_SECRET_PARAMETER_ | `--client_secret_parameter` _CLIENT_SECRET_PARAMETER_ | Name of the Key Vault Secrets parameter storing your API client secret |
|  `-u` _VAULT_URI_ | `--vault_uri` _VAULT_URI_ | URI of the Azure Key Vault containing the API credentials |

#### Basic usage
You must provide the Vault URI (`-u`) in order for this application to execute.

> If you choose to omit the *Client ID parameter* (`-k`) and *Client Secret parameter* (`-s`),
the default values `falcon-client-id` and `falcon-client-secret` will be used.

#### Example
Perform a simple API demonstration using the credentials retrieved to list hosts by AID.
```shell
python3 azure_key_vault.py -u https://example-kv-name.vault.azure.net/
```

##### Example result
```
Client API credentials successfully retrieved from Azure Key Vault.
host1 [a18sdfasdfasdfasafdf7cac44deb8d1]
host2 [asdfasdfuiuiwjkjlhxhjwdfkljh3891]
host3 [jlk2j3klnf289jflskjf02jfoi2j0jj3]
Demonstration completed.
```

#### Command-line help
Command-line help is available via the `-h` argument.

```
usage: azure_key_vault.py [-h] [-k CLIENT_ID_PARAMETER] [-s CLIENT_SECRET_PARAMETER] -u VAULT_URI

CrowdStrike API authentication leveraging Azure Key Vault for credential storage.
   _____
  /  _  \ __________ _________   ____
 /  /_\  \\___   /  |  \_  __ \_/ __ \
/    |    \/    /|  |  /|  | \/\  ___/
\____|__  /_____ \____/ |__|    \___  >
        \/      \/                  \/
     ____  __.             ____   ____            .__   __
    |    |/ _|____ ___.__. \   \ /   /____   __ __|  |_/  |_
    |      <_/ __ <   |  |  \   Y   /\__  \ |  |  \  |\   __\
    |    |  \  ___/\___  |   \     /  / __ \|  |  /  |_|  |
    |____|__ \___  > ____|    \___/  (____  /____/|____/__|

This application demonstrates storing CrowdStrike API credentials within the
Azure Key Vault service, and retrieving them to access the CrowdStrike API.

options:
  -h, --help            show this help message and exit
  -k CLIENT_ID_PARAMETER, --client_id_parameter CLIENT_ID_PARAMETER
                        Name of the Key Vault Secrets parameter storing your API client ID
  -s CLIENT_SECRET_PARAMETER, --client_secret_parameter CLIENT_SECRET_PARAMETER
                        Name of the Key Vault Secrets parameter storing your API client secret
  -u VAULT_URI, --vault_uri VAULT_URI
                        URI of the Azure Key Vault containing the API credentials
```

### Example source code
Source code for this example can be found [here](azure_key_vault.py).

---
## AES Authentication
Leverage AES/CBC to encrypt credentials for use with authentication to the CrowdStrike API.

> ⚠️ Please note ⚠️
>
> Cryptographic implementation samples should not be seen as recommendations on which encryption algorithms, modes or methods to use in your environment. These examples focus only on the technical aspects of cryptographic authentication scenarios using Python 3 and are provided here to assist developers with their implementation when interacting with the FalconPy SDK.

+ [Running the program](#running-the-program)
+ [Execution syntax](#execution-syntax)
+ [Example source code](#example-source-code)

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys with the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| Hosts | __READ__ |


### Execution syntax
This demonstration was developed to leverage easy to use command-line arguments.

- [Command line arguments](#command-line-arguments)
- [Basic usage](#basic-usage)
- [Running the demo](#example)
- [Generating a new credential file](#generating-a-new-credential-file)
- [Encrypting arbitrary text](#encrypting-arbitrary-text)
- [Decrypting arbitrary text](#decrypting-arbitrary-ciphertext)

#### Command line arguments
This program accepts the following command line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | Display command line help and exit |
|  `-t` _TEXT_ | `--text` _TEXT_ | Text to encrypt or decrypt |
|  `-k` _KEY_ | `--key` _KEY_ | Key to use for encryption operations |
|  `-f` _KEYFILE_ | `--keyfile` _KEYFILE_ | File to save your encrypted credentials to |
|  `-g` | `--generate` | Generate a new keyfile using a key you specify |
|  `-d` | `--decrypt` | Decrypt the value of _TEXT_ using the key provided in _KEY_. |
|  `-e` | `--encrypt` | Encrypt the value of _TEXT_ using the key provided in _KEY_. |

#### Basic usage
This program has no required command line arguments, and will prompt you to provide parameters expected for the operation requested.
For every operation, your _secret key_ (`-k`) and the location of your _key file_ (`-f`) can be passed to the program using command line arguments.

#### Example
Running without any arguments will attempt to consume a credential file and run the demo.
Providing a valid encrypted credential file and the correct _secret key_ at this point will start the procedure.
This test retrieves the hostname and AID for all hosts within the tenant.

```shell
python3 aes_authentication.py
```

##### Example result

```shell
  ❓ Please specify the file used to store your encrypted credentials: : credentials.enc
  ❓ Please provide your secret key :

  ✅ ID retrieval of 5223 hosts completed, requesting extended host details
  ⬇️  Downloading host detail from the CrowdStrike API for records 0 to 5000 of 5223 hosts, please wait...
  ⬇️  Downloading host detail from the CrowdStrike API for records 5000 to 5223 of 5223 hosts, please wait...
  ✅ Host detail retrieval complete, showing results.
  🖥  hostname-lcnhc                       [8a9337d325a84b4ea9b123456789abcd]
  🖥  hostname-h6vgb                       [c9df0f123456789abcd4313585190107]
  🖥  hostname-klz8t                       [cd5494123456789abcda3e22ba10841b]
  🖥  hostname-f4brn                       [123456789abcda6e8f09ec0f96319154]
  🖥  hostname-2zhvt                       [74b8c123456789abcda5ba60d6788f8e]
  🖥  hostname-czqzd                       [123abcdf160b46e4927ff4ffd3be95be]
```

#### Generating a new credential file
```shell
python3 aes_authentication.py -g
```

##### Example result

```shell
  ❓ Please provide your CrowdStrike API Client ID :
  ❓ Please provide your CrowdStrike API Client Secret :
  ❓ Please specify the file to use for storing your encrypted credentials: : credentials.enc
  ❓ Please provide your secret key :
```

#### Encrypting arbitrary text
This application can be used to encrypt arbitrary text. This operation does not interact with your credentials.

```shell
python3 aes_authentication.py -e -t "This is my test"
```

##### Arbitrary encryption result
```shell
  ❓ Please provide your secret key :
  🔐 Encrypted: qxbFiGLWpw26lygAqGGvM1Dwz569Ogemu/O+/QMYrxQ=
```

#### Decrypting arbitrary ciphertext
This application can be used to decrypt ciphertext as long as you have the correct secret key. This operation does not interact with your credentials.

```shell
python3 aes_authentication.py -d -t "qxbFiGLWpw26lygAqGGvM1Dwz569Ogemu/O+/QMYrxQ="
```

##### Ciphertext decryption result

```shell
  ❓ Please provide your secret key :
  🔓 Decrypted: This is my test
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: aes_authentication.py [-h] [-t TEXT] [-k KEY] [-f KEYFILE] [-g] [-d | -e]

Simple AES encryption example leveraging pyCryptodome.

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

optional arguments:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Text to encrypt or decrypt
  -k KEY, --key KEY     Key to use for encryption operations
  -f KEYFILE, --keyfile KEYFILE
                        File to save your encrypted credentials too
  -g, --generate        Generate a new keyfile using a key you specify
  -d, --decrypt         Decrypt the provided string
  -e, --encrypt         Encrypt the provided string
```

### Example source code
Source code for this example can be found [here](aes_authentication.py).

---

## AES File Crypt
This sample will encrypt and decrypt arbitrary files with AES/CBC using the secret key you provide.

> Not exactly useful for most real world scenarios, but I had a lot of fun writing the credential encryption example above and I couldn't stop playing with the code...

+ [Running the program](#running-the-program-1)
+ [Execution syntax](#execution-syntax-1)
+ [Example source code](#example-source-code-1)

### Running the program
This application does not require access to the CrowdStrike API.

### Execution syntax
This demonstration was developed to leverage easy to use command-line arguments.

- [Command line arguments](#command-line-arguments-1)
- [Basic usage](#basic-usage-1)
- [Example encryption](#example-encryption)
- [Example decryption](#example-decryption)
- [Calculating checksums](#calculating-checksums)
- [Changing the buffer size](#changing-the-buffer-size)

#### Command line arguments
This program accepts the following command line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | Display command line help and exit |
|  `-b` _BUFFER_ | `--buffer` _BUFFER_ | Maximum buffer size before the contents in memory are written to the target file. |
| `-c` | `--checksum` | MD5 / SHA256 hash the source / target file and display the result. |
|  `-d` | `--decrypt` | Decrypt from the _SOURCE_ to the _TARGET_. |
|  `-e` | `--encrypt` | Encrypt from the _SOURCE_ to the _TARGET_. |
|  `-k` _KEY_ | `--key` _KEY_ | Key to use for encryption and decryption operations. |
|  `-s` _SOURCE_ | `--source` _SOURCE_ | Source file to encrypt or decrypt. |
|  `-t` _TARGET_ | `--target` _TARGET_ | Target file for the resulting cryptographic operation. |


#### Basic usage
You must provide a key (`-k`), a source (`-s`), a target (`-t`) and an operation (`-d` or `-e`) in order for this application to execute.

#### Example encryption
Encrypting a file can be performed by providing a key, a source and a target file. For our examples, we'll use the following plain text file, `plain.txt`.

###### plain.txt
```text
This is my test plain text file.
I keep all my really important secrets in here.
Shhh!
```

The following command line will encrypt the contents of `plain.txt` to `cipher.txt` using the key `MySuperSecretKey`.

```shell
python3 aes_file_crypt.py -k MySuperSecretKey -s plain.txt -t cipher.txt -e
```

##### Encryption result

```shell
  🔐 Completed encryption of plain.txt to cipher.txt.
````

###### cipher.txt
```text
09PRhOrhM+kAH5J1fYglRufJc5DKcn0xT8P6XbaS9k13IUGUUsqRA4d16Us6lxeAWHjDYMSSJnTcx8UYgfa2jeRbxkKJJUZlmK2CGk08fcOqIfge42ktIpJQ/aZbCF/QdzYChLBislrh0s+oRAtgUQ==
```

#### Example decryption
Decrypting a file can be performed by providing a key, a source and a target file. For our examples, we'll use the cipher text file, `cipher.txt` we created above.

```shell
python3 aes_file_crypt.py -k MySuperSecretKey -s cipher.txt -t decrypted.txt -d
```

##### Encryption result

```shell
  🔓 Completed decryption of cipher.txt to decrypted.txt.
````

###### decrypted.txt
```text
This is my test plain text file.
I keep all my really important secrets in here.
Shhh!
```

#### Calculating checksums
You can hash the file when you encrypt or decrypt by passing the `-c` argument.
For encryption operations, this is performed on the _source_ file.
For decryption operations this occurs on the target file after the operation has completed.

##### Checksum on encryption

```shell
python3 aes_file_crypt.py -k MySuperSecretKey -s plain.txt -t cipher.txt -e -c
```

##### Checksum result on encryption

```shell
  #️⃣     MD5: e6073879c5e584bbdda5fb10fcac77a1
  #️⃣  SHA256: a3778bec2547a12d564a03618ac1e14c87271ad683c547246de520d54439d564
  🔐 Completed encryption of plain.txt to cipher.txt.
```

##### Checksum on decryption
```shell
python3 aes_file_crypt.py -k MySuperSecretKey -s cipher.txt -t decrypted.txt -d -c
```

##### Checksum result on decryption

```shell
  🔓 Completed decryption of cipher.txt to decrypted.txt.
  #️⃣     MD5: e6073879c5e584bbdda5fb10fcac77a1
  #️⃣  SHA256: a3778bec2547a12d564a03618ac1e14c87271ad683c547246de520d54439d564
```

#### Changing the buffer size
You may change the file buffer size to any value greater than or equal to 32. This alters the buffer pool size used when encrypting the file. This impacts cryptographic performance but does not alter the encryption used or the end result.

```shell
python3 aes_file_crypt.py -k MySuperSecretKey -s plain.txt -t cipher.txt -e -b 256
```

#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: aes_file_crypt.py [-h] -k KEY [-c] [-d] [-e] [-s SOURCE] [-t TARGET] [-b BUFFER]

Encrypt or decrypt a file with AES256/CBC encryption.

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

optional arguments:
  -h, --help            show this help message and exit
  -b BUFFER, --buffer BUFFER
                        Max buffer size before the contents are written to the target file.

behavior arguments:
  -c, --checksum        Print the hash of the target and source file arguments.
  -d, --decrypt         Decrypt from the source to the target.
  -e, --encrypt         Encrypt from the source to the target.

required arguments:
  -k KEY, --key KEY     Key to use for encryption and decryption operations.

file arguments:
  -s SOURCE, --source SOURCE
                        Source file to encrypt or decrypt.
  -t TARGET, --target TARGET
                        Target file for the resulting cryptographic operation.
```

### Example source code
Source code for this example can be found [here](aes_file_crypt.py).

---
## AWS Parameter store
This application demonstrates storing CrowdStrike API credentials within the AWS Parameter Store service, and retrieving them to access the CrowdStrike API.

### Running the program
In order to run this demonstration, you will need access to CrowdStrike API keys. You will also need to set your specific AWS location

#### Command line arguments
This program accepts the following command line arguments.

| Argument | Long Argument | Description |
| :-- | :-- | :-- |
| `-h` | `--help` | Display command line help and exit |
|  `-k` _CLIENT_ID_PARAMETER_ | `--client_id_parameter` _CLIENT_ID_PARAMETER_ | Name of the Key Vault Secrets parameter storing your API client ID |
|  `-s` _CLIENT_SECRET_PARAMETER_ | `--client_secret_parameter` _CLIENT_SECRET_PARAMETER_ | Name of the Key Vault Secrets parameter storing your API client secret |
|  `-d`  | `--debug`| Enables debugging functionality |

#### Basic usage

##### Use this command to test out the sample.

```shell
python3 aws_parameter_store.py -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET
```
##### Use this command to activate debugging.

```shell
python3 aws_parameter_store.py -k FALCON_CLIENT_ID -s FALCON_CLIENT_SECRET -d
```
#### Command-line help
Command-line help is available via the `-h` argument.

```shell
usage: aws_parameter_store.py [-h] [-k] CLIENT_ID [-s] CLIENT_SECRET [-d] DEGUG


  ___   ____    __    ____   _______.
    /   \  \   \  /  \  /   /  /       |
   /  ^  \  \   \/    \/   /  |   (----`
  /  /_\  \  \            /    \   \
 /  _____  \  \    /\    / .----)   |
/__/     \__\  \__/  \__/  |_______/

        ____                                  __               _____ __
       / __ \____ __________ _____ ___  ___  / /____  _____   / ___// /_____  ________
      / /_/ / __ `/ ___/ __ `/ __ `__ \/ _ \/ __/ _ \/ ___/   \__ \/ __/ __ \/ ___/ _ \
     / ____/ /_/ / /  / /_/ / / / / / /  __/ /_/  __/ /      ___/ / /_/ /_/ / /  /  __/
    /_/    \__,_/_/   \__,_/_/ /_/ /_/\___/\__/\___/_/      /____/\__/\____/_/   \___/


optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           enables degugging 

required arguments:
  -k CLIENT_ID, --client_id_parameter CLIENT_ID    
  -s CLIENT_SECRET, --client_secret_parameter CLIENT_SECRET
```


## Token Authentication
[Token authentication](https://www.falconpy.io/Usage/Authenticating-to-the-API.html#legacy-authentication) (also referred to as _legacy authentication_) is the process of authenticating to a FalconPy Service Class by providing a previously assigned bearer token directly to the [`auth_token`](https://www.falconpy.io/Usage/Basic-Service-Class-usage.html#legacy-authentication) keyword when instantiating the Service Class. This is the original method of authentication provided by Service Classes, and while it is frequently eschewed in preference to [Direct](https://www.falconpy.io/Usage/Authenticating-to-the-API.html#direct-authentication) and [Object](https://www.falconpy.io/Usage/Authenticating-to-the-API.html#object-authentication) [Authentication](https://www.falconpy.io/Usage/Authenticating-to-the-API.html), there are multiple scenarios where it is still the best option for the situation.

Token Authentication support will always be maintained within Falconpy.

> __⚠️ Please note ⚠️__
>
> Token Authentication creates an instance of a FalconPy Service Class that
> cannot reauthenticate itself as it does not have awareness of your API credentials. You will have to
> regenerate your bearer token before it expires and update the creds dictionary within the Service Class
> if you are implementing a long running process.

+ [Running the program](#running-the-program-2)
+ [Execution syntax](#execution-syntax-2)
+ [Example source code](#example-source-code-2)

### Running the program
This application is only a proof of concept that is intended to be reviewed as source code. Executing
the program will initiate a connectivity test to several CrowdStrike APIs. Credentials used for these
test are either stored in the environment (`FALCON_CLIENT_ID` and `FALCON_CLIENT_SECRET`) or requested
by the application when it starts.

In order for the demonstration to test all six API service collections, you will need access to the following scopes:
| Service Collection | Scope |
| :---- | :---- |
| CloudConnectAWS | __READ__ |
| Detects | __READ__ |
| Hosts | __READ__ |
| IOC | __READ__ |
| Incidents | __READ__ |
| Intel | __READ__ |

### Execution syntax
This application does not accept command line arguments.

#### Basic usage
This sample only supports singular execution.

```shell
python3 token_authentication_example.py
```

##### Example result

```shell
 CloudConnectAWS      [PASSED]
 Detects              [PASSED]
 Hosts                [PASSED]
 IOC                  [PASSED]
 Incidents            [PASSED]
 Intel                [PASSED]
```

#### Command-line help
This sample does not implement command line assistance.

### Example source code
Source code for this example can be found [here](token_authentication_example.py).
