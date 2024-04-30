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
inv = {"_meta": {"hostvars":{}},
        "app":   {"hosts": []},
        "db":    {"hosts": []},
        "docker-m": {"hosts": []}
        }
vms = get_vms()
#print (vms)
#print('\n\n\n')
inv2 = {}
inv2['_meta'] = {'hostvars':{}}
for vm in vms['instances']:
    try:
        g1 = vm['labels']['env']
        g2 = vm['labels']['tags']
        if g1 not in inv2:
            inv2[g1] = {'hosts': []}
        if g2 not in inv2:
            inv2[g2] = {'hosts': []}
        inv2[g1]['hosts'].append(vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address'])
        inv2[g2]['hosts'].append(vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address'])
    except:
        if "all" not in inv2:
            inv2['all'] = {'hosts': []}
        inv2['all']['hosts'].append(vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address'])

print(json.dumps(inv2))
#dbs = []
#for vm in vms['instances']:
#    print(vm)
#    if vm['labels']['tags'] == "reddit-app" and vm['labels']['env'] == "prod":
#        app = vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
#        inv['app']['hosts'].append(app)
#    if vm['labels']['tags'] == "reddit-db" and vm['labels']['env'] == "prod":
#        db = vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
#        inv['db']['hosts'].append(db)
#        dbs.append(vm['networkInterfaces'][0]['primaryV4Address']['address'])
#    if vm['labels']['env'] == "docker" and vm['labels']['tags'] == "monolith":
#        dm = vm['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']
#        inv['docker-m']['hosts'].append(dm)
#
#inv['app']['vars'] = {'dbs': dbs}
#print(json.dumps(inv))
