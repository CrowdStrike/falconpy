################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# oauth2 - Falcon X oAuth API Authentication Interface Class                                                   #
################################################################################################################
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class OAuth2:
    """ To create an instance of this class, you must pass a 
        properly formatted JSON object containing your falcon 
        client_id and falcon client_secret for the key you 
        wish to use to connect to the API.
        
        {
            "client_id": FALCON_CLIENT_ID,
            "client_secret": FALCON_CLIENT_SECRET
        }
    """

    def __init__(self, creds, base_url="https://api.crowdstrike.com"):
        """ Initializes the base class, ingesting credentials and the base URL. """
        self.creds = creds
        self.base_url = base_url

    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}

        def __call__(self, status_code, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['body'] = body
            
            return self.result_obj
    
    def token(self):
        """ Generates an authorization token. """
        FULL_URL = self.base_url+'/oauth2/token'
        HEADERS = {}
        DATA = {
            'client_id': self.creds['client_id'],
            'client_secret': self.creds['client_secret']
        }
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, data=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code,response.json())
        except Exception as e:
            returned = result(500, str(e))

        return returned
            
    def revoke(self, token):
        """ Revokes the specified authorization token. """
        FULL_URL = self.base_url+'/oauth2/revoke'
        HEADERS = { 'Authorization': 'basic {}'.format(token) }
        DATA = { 'token': '{}'.format(token) }
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, data=DATA, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.json())
        except Exception as e:
            returned = result(500, str(e))
            
        return returned
