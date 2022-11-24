from ._functions import generate_b64cred
from .._endpoint._oauth2 import _oauth2_endpoints as AuthEndpoints


def login_payloads(creds: dict, base: str):
    op_id = "oauth2AccessToken"
    target = f"{base}{[ep[2] for ep in AuthEndpoints if op_id in ep[0]][0]}"
    data = {
        'client_id': creds['client_id'],
        'client_secret': creds['client_secret']
    }
    if "member_cid" in creds:
        data["member_cid"] = creds["member_cid"]

    return op_id, target, data

def logout_payloads(creds: dict, base: str, token_val: str):
    op_id = "oauth2RevokeToken"
    target = f"{base}{[ep[2] for ep in AuthEndpoints if op_id in ep[0]][0]}"
    b64cred = generate_b64cred(creds["client_id"], creds["client_secret"])
    headers = {"Authorization": f"basic {b64cred}"}
    data = {"token": f"{token_val}"}

    return op_id, target, data, headers