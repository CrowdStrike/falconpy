"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

_util - Internal utilities library

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
import requests
import base64
import urllib3
from ._version import _title, _version
from ._result import Result
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# Restrict requests to only allowed HTTP methods
_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'UPDATE']
# Default user-agent string
_USER_AGENT = f"{_title}/{str(_version)}"


def validate_payload(validator: dict, params: dict, required: list = None) -> bool:
    """ Validates parameters and body payloads sent to the API """
    # Repurposed with permission from https://github.com/yaleman/crowdstrike_api
    #                                          __
    #                                         ( (\
    #                                          \ =\
    #                                         __\_ `--\
    #                                        (____))(  \----
    #                                        (____)) _     Thanks
    #                                        (____))       James!
    #                                        (____))____/----
    for key in params:
        if key not in validator:
            raise ValueError(f"{key} is not a valid argument.")
        if not isinstance(params[key], validator[key]):
            raise TypeError(f"{key} is not the valid type. Should be: {validator[key]}, was {type(params[key])}")
    if required:
        for key in required:
            if key not in params:
                raise ValueError(f"Argument {key} must be specified.")
    return True


def parse_id_list(id_list) -> str:
    """ Converts a list of IDs to a comma-delimited string """
    if type(id_list) is list:
        returned = ""
        for s in id_list:
            if len(returned) > 1:
                returned += ","
            returned += str(s)
        return returned
    else:
        return id_list


def generate_b64cred(client_id: str, client_secret: str) -> str:
    """ base64 encodes passed client_id and client_secret for authorization headers. """
    cr = "{}:{}".format(client_id, client_secret)
    b64_byt = base64.b64encode(cr.encode("ascii"))
    encoded = b64_byt.decode("ascii")

    return encoded


def service_request(caller: object = None, **kwargs) -> object:  # May return dict or object datatypes
    """ Checks for token expiration, refreshing if possible and then performs the request. """
    if caller:
        try:
            if caller.auth_object:
                if caller.auth_object.token_expired():
                    caller.auth_object.token()
                    caller.headers['Authorization'] = 'Bearer {}'.format(caller.auth_object.token()['body']['access_token'])
        except AttributeError:
            pass

    returned = perform_request(**kwargs)

    return returned


def perform_request(method: str = "", endpoint: str = "", headers: dict = None,
                    params: dict = None, body: dict = None, verify: bool = True,
                    data=None, files: list = [],
                    params_validator: dict = None, params_required: dict = None,
                    body_validator: dict = None, body_required: dict = None) -> object:  # May return dict or object datatypes
    """
        Leverages the requests library to perform the requested CrowdStrike OAuth2 API operation.

        method: str - HTTP method to use when communicating with the API
            - Example: GET, POST, PATCH, DELETE or UPDATE
        endpoint: str - API endpoint, do not include the URL base
            - Example: /oauth2/revoke
        headers: dict - HTTP headers to send to the API
            - Example: {"AdditionalHeader": "AdditionalValue"}
        params: dict - HTTP query string parameters to send to the API
            - Example: {"limit": 1, "sort": "state.asc"}
        body: dict - HTTP body payload to send to the API
            - Example: {"ids": "123456789abcdefg,987654321zyxwvutsr"}
        verify: bool - Enable / Disable SSL certificate checks
            - Example: True
        data - Encoded data to send to the API
            - Example: PAYLOAD = open(FILENAME, 'rb').read()
        files: list - List of files to upload
            - Example: [('file',('testfile2.jpg',open('testfile2.jpg','rb'),'image/jpeg'))]
        params_validator: dict - Dictionary containing parameters to be validated for the requested operation (key / datatype)
            - Example: { "limit": int, "offset": int, "filter": str}
        params_required: list - List of parameters required by the requested operation
            - Example: ["ids"]
        body_validator: dict - Dictionary containing payload to be validated for the requested operation (key / datatype)
            - Example: { "limit": int, "offset": int, "filter": str}
        body_required: list - List of payload parameters required by the requested operation
            - Example: ["ids"]
    """
    PERFORM = True
    METHOD = method.upper()
    if METHOD in _ALLOWED_METHODS:
        # Validate parameters
        if params_validator:
            try:
                validate_payload(params_validator, params, params_required)
            except ValueError as e:
                returned = generate_error_result(message=f"{str(e)}")
                PERFORM = False
            except TypeError as e:
                returned = generate_error_result(message=f"{str(e)}")
                PERFORM = False

        # Validate body payload
        if body_validator:
            try:
                validate_payload(body_validator, body, body_required)
            except ValueError as e:
                returned = generate_error_result(message=f"{str(e)}")
                PERFORM = False
            except TypeError as e:
                returned = generate_error_result(message=f"{str(e)}")
                PERFORM = False

        # Perform the request
        if PERFORM:
            headers["User-Agent"] = _USER_AGENT  # Force all requests to pass the User-Agent identifier
            try:
                response = requests.request(METHOD, endpoint, params=params, headers=headers,
                                            json=body, data=data, files=files, verify=verify)
                if response.headers.get('content-type') == "application/json":
                    returned = Result()(response.status_code, response.headers, response.json())
                else:
                    returned = response.content
            except Exception as e:
                returned = generate_error_result(message=f"{str(e)}")
    else:
        returned = generate_error_result(message="Invalid API operation specified.", code=405)

    return returned


def generate_error_result(message: str = "An error has occurred. Check your payloads and try again.", code: int = 500) -> dict:
    """ Normalized error messaging handler. """
    return Result()(status_code=code, headers={}, body={"errors": [{"message": f"{message}"}], "resources": []})


def generate_ok_result(message: str = "Request returned with success", code: int = 200) -> dict:
    return Result()(status_code=code, headers={}, body={"message": message, "resources": []})
