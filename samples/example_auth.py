#Example Auth.py file for use with scripts by Don-Swanson-Adobe
#Artifactory authentication (to upload to the repo)
afusername = 'crowdstrike'
afkey = 'EXAMPLE'

#CrowdStrike authentication
clientid = 'CLIENT_ID'
clientsec = 'CLIENT_SEC'

#List of Existing CIDs Formatted as a Dictionary with CID as the Key and CID Name as the Value
cids = {
    "123456789012345678901234567890": "CID1",
    "abcdefghijklmnopqrstuvwxyz1234": "CID2",
    "098765432109876543210987654321": "CID3",
    }

#List of NEW CIDs (Usable in the CID Transfer script)
new_cids = {
    "zz123456789012345678901234567890": "NEW_CID1",
    "zzabcdefghijklmnopqrstuvwxyz1234": "NEW_CID2",
    "zz098765432109876543210987654321": "NEW_CID3",
    }