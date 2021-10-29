"""Interactive debugger for the crowdstrike-falconpy project.

 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
import os
import sys
import importlib
import atexit
from os.path import dirname, join
import glob
from . import oauth2 as FalconAuth


def help(item=None):  # pylint: disable=W0622
    """Debugger help function. Overrides the built in python function."""
    text = """
    This is an interactive Python shell. Python help is available under python_help().

    AUTHENTICATION
    If you have FALCON_CLIENT_ID and FALCON_CLIENT_SECRET environment variables set,
    this shell will authenticate you at start up. You can also call the init()
    function passing the values dbg_falcon_client_id and dbg_falcon_client_secret, or
    you can pass a credential dictionary containing them.

    AVAILABLE VARIABLES
        'DEBUG_TOKEN' - your OAuth2 token.
        'AUTH_OBJECT' - an instance of the OAuth2 authorization class (authenticated).

    LISTING AVAILABLE SERVICE CLASSES
    Use list_modules() to retrieve a list of all available service classes.

    IMPORTING MODULES
    Use import_module("MODULE_NAME") to import any of the available service classes.

    Import hosts module and query for a specific host:
    In [1]: hosts = import_module("hosts")
    In [2]: hosts.QueryDevicesByFilter(filter="hostname:'whatever'")

    Importing the detects module and querying for all available detections with one command:
    In [1]: import_module("detects").QueryDetects()

    EXIT THE DEBUGGER
    Use exit / quit / CTRL-D to exit the debugger.
    """
    if item is None:
        print(text)
    elif callable(getattr(item, 'help', None)):
        item.help()
    else:
        print(item.__doc__)


def embed():
    """Embed the IPython interactive shell."""
    _ = importlib.import_module("IPython.terminal.embed")
    ipshell = _.InteractiveShellEmbed(banner1=BANNER)
    ipshell.confirm_exit = False
    ipshell()


def list_modules():
    """List all available Service Classes."""
    modules = glob.glob(join(dirname(__file__), "*.py"))
    result = []
    for key in modules:
        branched = key.split("/")
        position = len(branched)-1
        module_name = branched[position].replace(".py", "")
        if "_" not in module_name[0] and module_name not in ["debug", "api_complete"]:
            result.append(module_name)
    result.sort()
    print("Available modules")
    msg = ""
    for idx, val in enumerate(result):
        msg = f"{msg}%-35s" % val
        cnt = idx + 1
        if cnt % 2 == 0:
            print(msg)
            msg = ""
    print(msg)
    print("\nLoad modules with import_module('MODULE_NAME')")


def import_module(module: str = None):
    """Dynamically imports the module requested and returns an authenticated instance of the Service Class."""
    returned_object = False
    found = False
    if module:
        module = module.lower()
        import_location = "src.falconpy"
        try:
            # Assume they're working from the repo first
            _ = [importlib.import_module(f"{import_location}.{module}")]
            found = True
        except ImportError:
            try:
                import_location = "falconpy"
                # Then try to import from the installed module
                _ = [importlib.import_module(f"{import_location}.{module}")]
                found = True
            except ImportError:
                print("Unable to import requested service class")
        if found:
            current_module = sys.modules[f"{import_location}.{module}"]
            for key in dir(current_module):
                if isinstance(getattr(current_module, key), type) and not key == "ServiceClass" and "_" not in key:
                    _.append(getattr(_[0], key))
                    returned_object = _[1](auth_object=AUTH_OBJECT)
                    print(f"Service Class {key} imported successfully.")
    else:
        print("No module specified.")

    return returned_object


def exit_handler():
    """Revoke the DEBUG_TOKEN and gracefully quit the debugger. Overrides the built in python function."""
    if AUTH_OBJECT:
        print("Discarding token")
        AUTH_OBJECT.revoke(token=DEBUG_TOKEN)
    sys.exit(0)


def startup(dbg_falcon_client_id: str, dbg_falcon_client_secret: str):
    """Authenticate using the credentials provided and return the token / authentication object."""
    auth_object = FalconAuth.OAuth2(creds={
        'client_id': dbg_falcon_client_id,
        'client_secret': dbg_falcon_client_secret
    })

    try:
        debug_token = auth_object.token()["body"]["access_token"]
    except KeyError:
        debug_token = False
        auth_object = False

    return debug_token, auth_object


def init(dbg_falcon_client_id: str = None, dbg_falcon_client_secret: str = None, creds: dict = None):
    """Initialize the debugger by retrieving any available credentials and performing initial authentication."""
    if creds:
        dbg_falcon_client_id = creds["falcon_client_id"]
        dbg_falcon_client_secret = creds["falcon_client_secret"]

    if "FALCON_CLIENT_ID" in os.environ and "FALCON_CLIENT_SECRET" in os.environ:
        dbg_falcon_client_id = os.environ["FALCON_CLIENT_ID"]
        dbg_falcon_client_secret = os.environ["FALCON_CLIENT_SECRET"]

    global DEBUG_TOKEN, AUTH_OBJECT  # pylint: disable=W0603
    DEBUG_TOKEN, AUTH_OBJECT = startup(dbg_falcon_client_id, dbg_falcon_client_secret)
    embed()


# Move the internal python help() function to python_help()
python_help = help

# Configure our banner
BANNER = """
,---.     |                   ,--.      |
|__. ,---.|    ,---.,---.,---.|   |,---.|---..   .,---.
|    ,---||    |    |   ||   ||   ||---'|   ||   ||   |
`    `---^`---'`---'`---'`   '`--' `---'`---'`---'`---|
                                                  `---'
            CrowdStrike Python 3 Debug Interface

This shell-like interface allows for quick learning,
demoing, and prototyping of API operations using
the CrowdStrike FalconPy SDK and Python 3.

Please type help() to learn more.
                         |
     _____________   __ -+- _____________
     \\_____     /   /_ \\ |   \\     _____/
       \\_____   \\____/  \\____/    _____/
         \\_____    FalconPy      _____/
           \\___________  ___________/
                     /____\\
"""

# Default our debug token and auth object to False
DEBUG_TOKEN = False
AUTH_OBJECT = False

atexit.register(exit_handler)

init()
