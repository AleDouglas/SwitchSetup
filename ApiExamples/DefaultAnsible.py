import requests

def run_request(playbook, host,switch,username, password):
    url = 'http://127.0.0.1:8000/api/v1/'
    data = {
        'key': '0301a59375cf9b28783e122e5f5600e692ed432845c30a2aef1ba318efa0564d',
        'ansible_level': 0,
        'command': playbook,
        'host': host,
        'switch': switch,
        'username': username,
        'pasword': password,
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
