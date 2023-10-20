# 
#
#
#
#

import requests

def run_request():
    url = 'http://127.0.0.1:8000/api/v2/'
    data = {
        'key': '0301a59375cf9b28783e122e5f5600e692ed432845c30a2aef1ba318efa0564d',
        'ansible_level': 0,
        'playbook': '/backend/integrations/communs/custom/37e48b15-0de9-427f-8f39-a7d5c8cbc750.yml',
        'host': '/backend/integrations/communs/custom/1fec69fa-f03b-48c1-ae0d-70b6e98d0983.yml',
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        # Successful request, handle the response here
        result = response.json()
        print(result)
    else:
        # Error
        print('Error:', response.status_code)

if __name__ == '__main__':
    run_request()
