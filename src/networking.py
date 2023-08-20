import requests

def request_api(ip_address):
    api_url = 'http://ip-api.com/json/'
    full_url = f'{api_url}{ip_address}'

    response = requests.get(full_url)

    return response.status_code, response.json()
