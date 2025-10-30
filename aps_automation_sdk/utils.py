import requests
from typing import Annotated, Literal, Any

APS_BASE_URL = "https://developer.api.autodesk.com"
OSS_V2_BASE_URL = f"{APS_BASE_URL}/oss/v2"
DA_BASE_URL = f"{APS_BASE_URL}/da/us-east/v3" 
AUTH_URL = f"{APS_BASE_URL}/authentication/v2/token"

SCOPES = "data:read data:write data:create bucket:create bucket:read code:all"

def get_token(client_id: str, client_secret: str) -> str:
    response = requests.post(
        AUTH_URL,
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
            "scope": SCOPES,
        },
        timeout=15,
    )
    response.raise_for_status()
    token = response.json()["access_token"]
    return token

def get_nickname(token: str) -> str:
    url = f"{DA_BASE_URL}/forgeapps/me"
    r = requests.get(
        url,
        headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=30,
    )
    r.raise_for_status()
    # The API returns a JSON object with nickname and publicKey
    # Example response: {"nickname": "viktortest", "publicKey": {...}}
    response_data = r.json()
    return response_data.get("nickname", response_data)

def create_bucket(
    bucketKey: Annotated[str, "Unique Name you assign to a bucket, Possible values: -_.a-z0-9 (between 3-128 characters in length"],
    token: Annotated[str, "2Lo token"],
    policy_key: Literal["transient", "temporary", "persistent"]= "transient",
    access: None | Literal["full", "read"] = "full",
    region: Literal["US", "EMEA", "AUS", "CAN", "DEU", "IND", "JPN", "GBN"] = "US",
) -> dict[str, Any]:
    """
    Create a bucket in OSS v2.
    https://aps.autodesk.com/en/docs/data/v2/reference/http/buckets-POST/
    """
    url = f"{OSS_V2_BASE_URL}/buckets"
    payload = {"bucketKey": bucketKey, "access": access, "policyKey": policy_key}
    headers = {
        "Authorization":f"Bearer {token}",
        "Content-Type": "application/json",
        "x-ads-region": region,
    }
    r = requests.post(url, headers=headers, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()

def delete_appbundle(appbundleId:str, token: str) -> int:
    url = f"{DA_BASE_URL}/appbundles/{appbundleId}"
    header = {"Authorization": f"Bearer {token}"}
    r = requests.delete(url=url, headers=header)
    r.raise_for_status() 
    return r.status_code

def delete_activity(activityId: str, token: str) -> int:
    url = f"{DA_BASE_URL}/activities/{activityId}"
    header = {"Authorization": f"Bearer {token}"}
    r = requests.delete(url=url, headers=header)
    r.raise_for_status()
    return r.status_code
