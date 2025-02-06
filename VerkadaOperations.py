import requests
import os
from dotenv import load_dotenv

token = ""

def get_api_token():
    load_dotenv()

    api_key = os.environ.get('API_KEY')

    url = 'https://api.verkada.com/token'
    headers = {'accept': 'application/json','x-api-key': api_key}

    r = requests.post(url, headers=headers)
    

    token = r.json()['token']
    return token
    
def getdoorids():
    url = "https://api.verkada.com/access/v1/doors"

    headers = {
    "accept": "application/json",
    "x-verkada-auth": token
    }

    response = requests.get(url, headers=headers)
    response = response.json()

    doorids = []
    i = 0
    for key in response["doors"]:
        doorids.append(response["doors"][i]["door_id"])
        i +=1
        ###this may be trivially solvable with a for loop
    return(doorids)

token = get_api_token()
print(getdoorids())