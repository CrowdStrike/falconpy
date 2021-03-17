import os
from . import oauth2 as FalconAuth

banner = """
CrowdStrike Cloud Demo Shell                                          |
                                                  ____________    __ -+-  ____________
This shell-like wizard allows for quick learning, \\_____     /   /_ \\ |   \\     _____/
demoing, and prototyping of cloud operations with  \\_____    \\____/  \\____/    _____/
CrowdStrike Falcon agent.                           \\_____                    _____/
                                                       \\___________  ___________/
Please issue help() to learn more.                               /____\\
"""


python_help = help


def help(item=None):
    text = """
    This is interactive Python shell. Python help is available under python_help()

    If you have FALCON_CLIENT_ID FALCON_CLIENT_SECRET environment variable set. This
    shell will authenticate at the start up and token variable will be filled in with
    OAuth2 token.
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


falcon_client_id = os.getenv("FALCON_CLIENT_ID")
falcon_client_secret = os.getenv("FALCON_CLIENT_SECRET")

authorization = FalconAuth.OAuth2(creds={
    'client_id': falcon_client_id,
    'client_secret': falcon_client_secret
})

try:
    token = authorization.token()["body"]["access_token"]
except:
    token = False

embed()
