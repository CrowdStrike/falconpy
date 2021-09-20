"""Internal payload handling library

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


def create_generic_payload_list(submitted_keywords: dict,
                                payload_value: str,
                                submitted_arguments: list = None
                                ) -> dict:
    """Creates a standardized BODY payload based upon the
    requested payload value and passed keywords.

    Resulting payload provides passed keywords values in list format.

    Creates the following payload:
    {
      "payload_value": [
        "keyword provided values"
      ]
    }
    """
    returned_payload = {}
    submitted_values = submitted_keywords.get(payload_value, None)
    if submitted_values:
        if not isinstance(submitted_values, list):
            submitted_values = submitted_values.split(",")
        returned_payload[payload_value] = submitted_values
    else:
        if submitted_arguments:
            if isinstance(submitted_arguments[0], dict):
                # They're passing us a full payload
                returned_payload = submitted_arguments[0]
            else:
                # They're just passing us values
                submitted_values = submitted_arguments[0]
                if not isinstance(submitted_values, list):
                    submitted_values = submitted_values.split(",")
                returned_payload[payload_value] = submitted_values

    return returned_payload
