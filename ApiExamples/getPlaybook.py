# 
#
#
#
#

import requests

def run_request():
    url = 'http://127.0.0.1:8000/api/v3/playbook'
    data = {
        'key': '0301a59375cf9b28783e122e5f5600e692ed432845c30a2aef1ba318efa0564d',
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
