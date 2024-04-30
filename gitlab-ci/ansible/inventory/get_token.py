import time
import jwt
import json
import requests

def get_token():
    with open('/home/administrator/key.json', 'r') as key:
        rkey = key.read()
        p_key = json.loads(rkey)["private_key"]
        service_acc_id = json.loads(rkey)["service_account_id"]
        key_id = json.loads(rkey)["id"]

    now = int(time.time())
    payload = {
            'aud': 'https://iam.api.cloud.yandex.net/iam/v1/tokens',
            'iss': service_acc_id,
            'iat': now,
            'exp': now + 360
            }
    enc_token = jwt.encode(
            payload,
            p_key,
            algorithm = "PS256",
            headers = {'kid': key_id}
            )

    r = requests.post("https://iam.api.cloud.yandex.net/iam/v1/tokens", json={"jwt": str(enc_token)})
    return json.loads(r.text)['iamToken']

if __name__ == '__main__':
    get_token()
