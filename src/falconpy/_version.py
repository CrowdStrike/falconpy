"""Internal version control constants.

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
_VERSION = '1.3.0.dev6'
_MAINTAINER = 'Joshua Hiller'
_AUTHOR = 'CrowdStrike'
_AUTHOR_EMAIL = 'falconpy@crowdstrike.com'
_CREDITS = 'CrowdStrike'
_DESCRIPTION = "The CrowdStrike Falcon SDK for Python 3"
_TITLE = "crowdstrike-falconpy"
_PROJECT_URL = "https://github.com/CrowdStrike/falconpy"
_DOCS_URL = "https://www.falconpy.io"
_KEYWORDS = ["crowdstrike", "falcon", "api", "sdk", "oauth2", "devsecops", "crowdstrike-falcon"]


def version(compare: str = None, agent_string: bool = None):
    """Provide a callable method for checking and comparing the current FalconPy version.

    Keyword arguments
    ----
    agent_string: bool
        Boolean flag indicating that the default User-Agent string should
        be returned instead.
    compare: str
        String representation of the version to compare against.
        Returns True when the current version is greater or equal to the comparison value.
        Examples: "1", "1.3" or "1.3.0"

    Returns
    ----
    str or bool
        A string containing the requested version detail or a boolean indicating the status
        of the requested version comparison.
    """
    returned = _VERSION
    if agent_string:
        returned = f"{_TITLE}/{str(_VERSION)}"

    if compare:
        returned = False
        ver = _VERSION.split(".")
        chk = compare.split(".")
        chk_minor = 0
        chk_patch = 0
        if chk:
            chk_major = chk[0]
        if len(chk) > 1:
            chk_minor = chk[1]
        if len(chk) > 2:
            chk_patch = int(chk[2])
        major_minor = float(f"{ver[0]}.{ver[1]}")
        chk_major_minor = float(f"{chk_major}.{chk_minor}")
        if major_minor > chk_major_minor:
            returned = True
        elif major_minor == chk_major_minor and int(ver[2]) >= chk_patch:
            returned = True

    return returned
