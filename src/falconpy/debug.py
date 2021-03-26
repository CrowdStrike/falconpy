from . import oauth2 as FalconAuth

banner = """
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

python_help = help


def help(item=None):
    text = """
    This is interactive Python shell. Python help is available under python_help()
    If you have FALCON_CLIENT_ID FALCON_CLIENT_SECRET environment variable set. This
    shell will authenticate at the start up and the 'debug_token' variable will be
    filled in with your OAuth2 token.
    """
    if item is None:
        print(text)
    elif callable(getattr(item, 'help', None)):
        item.help()
    else:
        print(item.__doc__)


def embed():
    from IPython.terminal.embed import InteractiveShellEmbed
    ipshell = InteractiveShellEmbed(banner1=banner)
    ipshell.confirm_exit = False
    ipshell()


def startup(dbg_falcon_client_id: str, dbg_falcon_client_secret: str):
    dbg_authorization = FalconAuth.OAuth2(creds={
        'client_id': dbg_falcon_client_id,
        'client_secret': dbg_falcon_client_secret
    })

    try:
        debug_token = dbg_authorization.token()["body"]["access_token"]
    except Exception:
        debug_token = False

    return debug_token


def init(dbg_falcon_client_id: str = None, dbg_falcon_client_secret: str = None, creds: dict = None):
    if creds:
        dbg_falcon_client_id = creds["falcon_client_id"]
        dbg_falcon_client_secret = creds["falcon_client_secret"]
    global debug_token
    debug_token = startup(dbg_falcon_client_id, dbg_falcon_client_secret)
    embed()


debug_token = False
