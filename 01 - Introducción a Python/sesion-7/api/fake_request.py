import json
import requests

# Desafio 1
URL = 'https://reqres.in/api/users'


def request(method, url, payload=""):
    headers = {
        'Content-Type': "application/json",
    }
    response = requests.request(method, url, data=payload, headers=headers)
    if method == 'DELETE':
        return response
    return json.loads(response.text)


# Desafio 2
print(request('GET', URL))

# Desafio 3
chewy_payload = json.dumps({'name': 'Chewy', 'job': 'Spy'})
chewy_response = request('POST', URL, chewy_payload)
print(chewy_response)

# Desafio 4
chewy_id = chewy_response['id']
chewy_update_payload = json.dumps({'name': 'Chewy', 'job': 'President'})
print(request('PUT', URL + '/' + chewy_id, chewy_update_payload))

# Desafio 5
print(request('DELETE', 'https://reqres.in/api/users/api/users/2'))
