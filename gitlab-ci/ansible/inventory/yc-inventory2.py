#!/usr/bin/env python
import json
import requests
from get_token import get_token
def get_vms():
    session = requests.Session()
    token = get_token()
    vms = session.get("https://compute.api.cloud.yandex.net/compute/v1/instances",
                      headers={"Authorization": "Bearer " + token},
                      params={'folderId': 'b1gu9td5uk8ohab1ecp8'}
                      )
    return json.loads(vms.text)

# => vms a dictionary (basicaly json)
vms = get_vms()
#print (vms)
#print('\n\n\n')
inv2 = {}
inv2['_meta'] = {'hostvars':{}}
for vm in vms['instances']:
    host_ip = vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
    try:
        for label in vm['labels']:
            if vm['labels'][label] not in inv2:
                inv2[vm['labels'][label]] = {'hosts': []}
            inv2[vm['labels'][label]]['hosts'].append(host_ip)
    except:
        if "all" not in inv2:
            inv2['all'] = {'hosts': []}
        inv2['all']['hosts'].append(host_ip)
    inv2['_meta']['hostvars'][host_ip] = {'self_natip': host_ip}
print(json.dumps(inv2))
