"""Internal utilities library.

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
import base64
import functools
from json.decoder import JSONDecodeError
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from ._version import _TITLE, _VERSION
from ._result import Result, ExpandedResult
from ._base_url import BaseURL
from ._container_base_url import ContainerBaseURL
from ._uber_default_preference import PREFER_NONETYPE, MOCK_OPERATIONS
urllib3.disable_warnings(InsecureRequestWarning)

# Restrict requests to only allowed HTTP methods
_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'UPDATE']
# Default user-agent string
_USER_AGENT = f"{_TITLE}/{str(_VERSION)}"


def validate_payload(validator: dict, params: dict, required: list = None) -> bool:
    """Validate parameters and body payloads sent to the API."""
    # Repurposed with permission from
    # https://github.com/yaleman/crowdstrike_api
    #         __
    #        ( (\
    #         \ =\
    #        __\_ `--\
    #       (____))(  \----
    #       (____)) _     Thanks
    #       (____))       James!
    #       (____))____/----
    #
    if required:
        for key in required:
            if key not in params:
                raise ValueError(f"Argument {key} must be specified.")

    for key in params:
        if key not in validator:
            raise ValueError(f"{key} is not a valid argument.")
        if not isinstance(params[key], validator[key]):
            should = validator[key]
            was = type(params[key])
            raise TypeError(f"{key} is not the valid type. Should be: {should}, was {was}")

    return True


def generate_b64cred(client_id: str, client_secret: str) -> str:
    """base64 encodes passed client_id and client_secret for authorization headers."""
    cred = f"{client_id}:{client_secret}"
    b64_byt = base64.b64encode(cred.encode("ascii"))
    encoded = b64_byt.decode("ascii")

    return encoded


def handle_single_argument(passed_arguments: list, passed_keywords: dict, search_key: str) -> dict:
    """Handle a single argument that is provided without keywords.

    Reviews arguments passed to a method and injects them into the keyword dictionary if they
    match the search string.
    """
    if len(passed_arguments) > 0:
        passed_keywords[search_key] = passed_arguments[0]

    return passed_keywords


def force_default(defaults: list, default_types: list = None):
    """Force default values.

    Intended to decorate other functions.

    Keyword arguments:
    defaults = list of values to default
    default_types = list of types to default the values to

    Example: @force_default(defaults=["parameters], default_types=["dict"])
    """
    if not default_types:
        default_types = []

    def wrapper(func):
        """Inner wrapper."""
        @functools.wraps(func)
        def factory(*args, **kwargs):
            """Parameter factory.

            This method is a factory and runs through keywords passed to the called function,
            setting defaults on values within the **kwargs dictionary when necessary
            as specified in our "defaults" list that is passed to the parent wrapper.
            """
            element_count = 0   # Tracker so we can retrieve matching data types
            # Loop through every element specified in our defaults list
            for element in defaults:
                if element in kwargs:
                    # It exists but it's a NoneType
                    if kwargs.get(element) is None:
                        kwargs[element] = get_default(default_types, element_count)
                else:
                    # Not present whatsoever
                    kwargs[element] = get_default(default_types, element_count)
                # Increment our tracker for our sibling default_types list
                element_count += 1

            try:
                created = func(*args, **kwargs)
            except TypeError:
                # They passed us an argument but did not specify what it was (non-keyword) [Issue #263]
                created = generate_error_result("Keyword arguments must be used for this method.")

            return created
        return factory
    return wrapper


def service_request(caller: object = None, **kwargs) -> object:  # May return dict or object datatypes
    """Check for token expiration, refresh if possible and then perform the request."""
    if caller:
        try:
            if caller.auth_object:
                if caller.auth_object.token_expired():
                    auth_response = caller.auth_object.token()
                    if auth_response["status_code"] == 201:
                        caller.headers['Authorization'] = f"Bearer {auth_response['body']['access_token']}"
                    else:
                        caller.headers['Authorization'] = "Bearer "
                else:
                    caller.headers['Authorization'] = f"Bearer {caller.auth_object.token_value}"
        except AttributeError:
            pass

        try:
            proxy = caller.proxy
        except AttributeError:
            proxy = None

        try:
            timeout = caller.timeout
        except AttributeError:
            timeout = None

        try:
            user_agent = caller.user_agent
        except AttributeError:
            user_agent = None

    returned = perform_request(proxy=proxy, timeout=timeout, user_agent=user_agent, **kwargs)

    return returned


@force_default(defaults=["headers"], default_types=["dict"])
def perform_request(endpoint: str = "",  # pylint: disable=R0912
                    headers: dict = None,
                    **kwargs
                    ) -> object:  # May return dict or object data types
    """Leverage the requests library to perform the requested CrowdStrike OAuth2 API operation.

    Keyword arguments:
    method: str - HTTP method to use when communicating with the API
        - Example: GET, POST, PATCH, DELETE or UPDATE
    endpoint: str - API endpoint, including the URL base
        - Example: https://api.crowdstrike.com/oauth2/revoke
    headers: dict - HTTP headers to send to the API
        - Example: {"AdditionalHeader": "AdditionalValue"}
    params: dict - HTTP query string parameters to send to the API
        - Example: {"limit": 1, "sort": "state.asc"}
    body: dict - HTTP body payload to send to the API
        - Example: {"ids": ["123456789abcdefg", "987654321zyxwvutsr"]}
    verify: bool - Enable / Disable SSL certificate checks
        - Example: True
    data - Encoded data to send to the API
        - Example: PAYLOAD = open(FILENAME, 'rb').read()
    files: list - List of files to upload
        - Example: [('file',('testfile2.jpg',open('testfile2.jpg','rb'),'image/jpeg'))]
    body_validator: dict - Dictionary containing payload to be validated for the requested operation (key / datatype)
        - Example: { "limit": int, "offset": int, "filter": str}
    body_required: list - List of payload parameters required by the requested operation
        - Example: ["ids"]
    proxy: dict - Dictionary containing a list of proxies to use for requests
        - Example: {"https": "https://myproxy.com:4000", "http": "http://myhttpproxy:80"}
    timeout: float or tuple
        Float representing the global timeout for requests or a tuple containing the connect / read timeouts.
        - Example: 30
        - Example: (5.05, 25)
    user_agent: string
        - Example: companyname-integrationname/version
    expand_result: bool - Enable expanded results output
        - Example: True
    container: bool - Is this request being sent to a Falcon Container registry endpoint
        - Example: False
    """
    method = kwargs.get("method", "GET")
    body = kwargs.get("body", None)
    body_validator = kwargs.get("body_validator", None)
    user_agent = kwargs.get("user_agent", None)
    expand_result = kwargs.get("expand_result", False)
    perform = True
    if method.upper() in _ALLOWED_METHODS:
        # Validate parameters
        # 05.21.21/JSH - Param validation is now handled by the updated args_to_params method

        # Validate body payload
        if body_validator:
            try:
                validate_payload(body_validator, body, kwargs.get("body_required", None))
            except ValueError as err:
                returned = generate_error_result(message=f"{str(err)}")
                perform = False
            except TypeError as err:
                returned = generate_error_result(message=f"{str(err)}")
                perform = False

        # Perform the request
        if perform:
            if user_agent:
                headers["User-Agent"] = user_agent
            else:
                headers["User-Agent"] = _USER_AGENT  # Force all requests to pass the User-Agent identifier
            headers["CrowdStrike-SDK"] = _USER_AGENT
            try:
                response = requests.request(method.upper(), endpoint, params=kwargs.get("params", None),
                                            headers=headers, json=kwargs.get("body", None), data=kwargs.get("data", None),
                                            files=kwargs.get("files", []), verify=kwargs.get("verify", True),
                                            proxies=kwargs.get("proxy", None), timeout=kwargs.get("timeout", None)
                                            )
                # Force binary when content-type is not provided
                returning_content_type = response.headers.get('content-type', "Binary")
                if returning_content_type.startswith("application/json"):  # Issue 708
                    content_return = Result()(response.status_code, response.headers, response.json())
                elif kwargs.get("container", False):
                    content_return = Result()(response.status_code, response.headers, response.json())
                else:
                    content_return = response.content
                # Expanded results allow for status code and header checks on binary returns
                if expand_result:
                    returned = ExpandedResult()(response.status_code, response.headers, content_return)
                else:
                    returned = content_return

            except JSONDecodeError:  # pragma: no cover
                # No response content, but a successful request was made
                returned = generate_ok_result(
                    message="No content returned",
                    code=response.status_code,
                    headers=response.headers
                    )
            except Exception as err:  # pylint: disable=W0703  # General catch-all for anything coming out of requests
                returned = generate_error_result(message=f"{str(err)}")
    else:
        returned = generate_error_result(message="Invalid API operation specified.", code=405)

    return returned


def generate_error_result(
        message: str = "An error has occurred. Check your payloads and try again.",
        code: int = 500,
        **kwargs
        ) -> dict:
    """Normalize error messages."""
    return_headers = kwargs.get("headers", {})
    return Result()(status_code=code, headers=return_headers, body={"errors": [{"message": f"{message}"}], "resources": []})


def generate_ok_result(message: str = "Request returned with success", code: int = 200, **kwargs) -> dict:
    """Normalize OK messages."""
    return_headers = kwargs.get("headers", {})
    return Result()(status_code=code, headers=return_headers, body={"message": message, "resources": []})


def get_default(types: list, position: int):
    """I determine the requested default data type and return it."""
    default_value_names = ["list", "str", "int", "dict", "bool"]
    default_value_types = [[], "", 0, {}, False]
    value_count = 0
    retval = {}  # Default to dictionary data type as that is our most often used
    for type_ in default_value_names:
        try:
            if type_ in types[position]:
                retval = default_value_types[value_count]
        except IndexError:
            # Data type not specified, fall back to dictionary
            pass
        value_count += 1

    return retval


def args_to_params(payload: dict, passed_arguments: dict, endpoints: list, epname: str) -> dict:
    """Query String parameter abstraction handler.

    This function reviews arguments passed to the function against arguments accepted by the
    endpoint. If a valid argument is passed, it is added and returned as part of the QueryString
    payload dictionary.

    This function will convert passed comma-delimited strings to list data types when necessary.

    The method only handles QueryString parameters, and will skip any Body payload parameters it
    encounters.

    When using override functionality via the Uber class, this method skips processing. (Override
    functionality does not support QueryString parameter abstraction.)

    Keyword arguments:
    payload -- Existing QueryString parameter payload. Dictionary.
    passed_arguments -- Keywords provided to the calling method.
    endpoints -- List of API endpoints available to the calling method.
    epname -- Operation ID to be retrieved from the endpoints list.

    Returns: dictionary representing QueryString parameters.
    """
    returned_payload = {}
    if epname != "Manual":  # pylint: disable=R1702
        for arg in passed_arguments:
            eps = [ep[5] for ep in endpoints if epname == ep[0]][0]
            try:
                argument = [param for param in eps if param["name"] == arg][0]
                if argument:
                    arg_name = argument["name"]
                    if "type" in argument:  # Body payload parameters do not have a type field
                        if argument["type"] == "array":
                            if isinstance(passed_arguments[arg_name], (str)):
                                passed_arguments[arg_name] = passed_arguments[arg_name].split(",")
                        # More data type validation can go here
                        payload[arg_name] = passed_arguments[arg_name]
            except IndexError:
                # Unrecognized argument
                pass

    # Clean up reserved word conversions when passing in an invalid raw payload
    if payload:
        for element in payload:
            if not isinstance(element, str):
                returned_payload[element.__name__] = payload[element]
            else:
                returned_payload[element] = payload[element]

    return returned_payload


def process_service_request(calling_object: object,  # pylint: disable=R0914 # (19/15)
                            endpoints: list,
                            operation_id: str,
                            **kwargs
                            ) -> dict:
    """Perform a request originating from a service class module.

    Calculates the target_url based upon the provided operation ID and endpoint list.

    Keyword arguments:
    endpoints -- list - List of service class endpoints, defined as Endpoints in a service class. [required]
    operation_id -- The name of the operation ID. Normally this is also the function name from the service class. [required]
    method -- HTTP method to execute. GET, POST, PATCH, DELETE, PUT accepted. Defaults to GET.
    keywords -- Dictionary of kwargs that were passed to the function within the service class.
    params -- Dictionary of parameters passed to the service class function.
    headers -- Dictionary of headers passed to and calculated by the service class function.
    body -- Dictionary representing the body payload passed to the service class function.
    data -- Dictionary representing the data payload passed to the service class function.
    files -- List of files to be uploaded.
    partition -- ID of the partition to open (Event Streams API)
    distinct_field -- Field name to retrieve distinct values for (Sensor Update Policies API)
    image_id -- Image ID to be deleted (Falcon Container API)
    body_validator -- Dictionary containing details regarding body payload validation
    body_required -- List of required body payload parameters
    expand_result -- Request expanded results output
    """
    target_endpoint = [ep for ep in endpoints if operation_id == ep[0]][0]
    base_url = calling_object.base_url
    container = False
    if operation_id in MOCK_OPERATIONS:
        for base in [burl for burl in dir(BaseURL) if "__" not in burl]:
            if BaseURL[base].value == calling_object.base_url.replace("https://", ""):
                base_url = f"https://{ContainerBaseURL[base].value}"
                container = True
    target_url = f"{base_url}{target_endpoint[2]}"
    target_method = target_endpoint[1]
    passed_partition = kwargs.get("partition", None)
    if passed_partition or isinstance(passed_partition, int):
        target_url = target_url.format(str(passed_partition))
    passed_distinct_field = kwargs.get("distinct_field", None)
    if passed_distinct_field:
        target_url = target_url.format(str(passed_distinct_field))
    passed_image_id = kwargs.get("image_id", None)
    if passed_image_id:
        target_url = target_url.format(str(passed_image_id))
    # Retrieve our keyword arguments
    passed_keywords = kwargs.get("keywords", None)
    passed_params = kwargs.get("params", None)
    parameter_payload = None
    if passed_keywords or passed_params:
        parameter_payload = args_to_params(passed_params, passed_keywords, endpoints, operation_id)
    passed_headers = kwargs.get("headers", None) if kwargs.get("headers", None) else calling_object.headers
    expand_result = passed_keywords.get("expand_result", False) if passed_keywords else kwargs.get("expand_result", False)
    new_keywords = {
        "caller": calling_object,
        "method": target_method,
        "endpoint": target_url,
        "verify": calling_object.ssl_verify,
        "headers": passed_headers,
        "params": parameter_payload,
        "body": kwargs.get("body", None),
        "data": kwargs.get("data", None),
        "files": kwargs.get("files", None),
        "body_validator": kwargs.get("body_validator", None),
        "body_required": kwargs.get("body_required", None),
        "expand_result": expand_result,
        "container": container
    }

    return service_request(**new_keywords)


def confirm_base_url(provided_base: str = "https://api.crowdstrike.com") -> str:
    """Confirm the passed base_url value matches URL syntax.

    If it does not, it is looked up in the BaseURL enum. If the value is not found
    within the enum, https:// is prepended to the value and then it is used for API requests.
    """
    # Assume they passed a full URL
    returned_base = provided_base
    if "://" not in provided_base:
        # They're passing the name instead of the URL
        dashed_bases = ["US-1", "US-2", "EU-1", "US-GOV-1"]
        if provided_base.upper() in dashed_bases:
            provided_base = provided_base.replace("-", "")  # Strip the dash
        try:
            returned_base = f"https://{BaseURL[provided_base.upper()].value}"
        except KeyError:
            # Invalid base URL name, fall back to assuming they didn't give us https
            returned_base = f"https://{provided_base}"

    if returned_base[-1] == "/":  # Issue 558
        returned_base = returned_base[:-1]

    return returned_base


def confirm_base_region(provided_base_url: str = "https://api.crowdstrike.com") -> str:
    """Retrieve the base url shortname based upon the provided base url value."""
    try:
        shortname = BaseURL(provided_base_url.replace("https://", "").lower()).name
    except (KeyError, ValueError):
        shortname = "US1"  # Fall back to US-1

    return shortname


def return_preferred_default(method_name: str = None, keyword_type: str = "dict"):
    """Use the PREFER_NONETYPE list lookup to determine the default to use for empty payloads."""
    default_return = {}
    if method_name:
        if keyword_type.lower() == "list":
            default_return = []
        if method_name in PREFER_NONETYPE:
            default_return = None

    return default_return


def base_url_regions():
    """Return a list of available Base URL regions."""
    return [bu.name for bu in BaseURL]


def autodiscover_region(provided_base_url: str, auth_result: dict):
    """Autodiscovers the correct region for the token response."""
    new_base_url = confirm_base_url(provided_base_url)
    # Swap to the correct region if they've provided the incorrect one
    if "X-Cs-Region" not in auth_result["headers"]:  # pragma: no cover
        # Starting in v1.2.4, us-gov-1 headers are returned
        # but autoselection is still unsupported
        token_region = confirm_base_region(confirm_base_url(provided_base_url))
    else:
        token_region = auth_result["headers"]["X-Cs-Region"].replace("-", "")
    if token_region.upper() in base_url_regions():
        requested_region = confirm_base_region(confirm_base_url(provided_base_url))
        if token_region != requested_region:
            new_base_url = confirm_base_url(token_region.upper())

    return new_base_url
