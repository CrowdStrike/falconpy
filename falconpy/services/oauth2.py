################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# oAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# oauth2 - Falcon X oAuth API Authentication Interface Class                                                   #
################################################################################################################
# Copyright CrowdStrike 2020

# By accessing or using this script, sample code, application programming interface, tools, 
# and/or associated documentation (if any) (collectively, “Tools”), You (i) represent and 
# warrant that You are entering into this Agreement on behalf of a company, organization 
# or another legal entity (“Entity”) that is currently a customer or partner of 
# CrowdStrike, Inc. (“CrowdStrike”), and (ii) have the authority to bind such Entity and 
# such Entity agrees to be bound by this Agreement.

# CrowdStrike grants Entity a non-exclusive, non-transferable, non-sublicensable, royalty 
# free and limited license to access and use the Tools solely for Entity’s internal business 
# purposes and in accordance with its obligations under any agreement(s) it may have with 
# CrowdStrike. Entity acknowledges and agrees that CrowdStrike and its licensors retain all 
# right, title and interest in and to the Tools, and all intellectual property rights 
# embodied therein, and that Entity has no right, title or interest therein except for the 
# express licenses granted hereunder and that Entity will treat such Tools as CrowdStrike’s 
# confidential information.

# THE TOOLS ARE PROVIDED “AS-IS” WITHOUT WARRANTY OF ANY KIND, WHETHER EXPRESS, IMPLIED OR 
# STATUTORY OR OTHERWISE. CROWDSTRIKE SPECIFICALLY DISCLAIMS ALL SUPPORT OBLIGATIONS AND 
# ALL WARRANTIES, INCLUDING WITHOUT LIMITATION, ALL IMPLIED WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR PARTICULAR PURPOSE, TITLE, AND NON-INFRINGEMENT. IN NO EVENT SHALL CROWDSTRIKE 
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THE TOOLS, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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
