import requests
import os
from dotenv import load_dotenv

def get_api_token():
    load_dotenv()

    api_key = os.environ.get('API_KEY')

    url = 'https://api.verkada.com/token'
    headers = {'accept': 'application/json','x-api-key': api_key}

    r = requests.post(url, headers=headers)
    

    token = r.json()['token']
    return token
    

get_api_token()