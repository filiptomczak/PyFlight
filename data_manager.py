import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_API = os.environ.get('SHEETY_API')

class DataManager:
    def __init__(self):
        self.header={
            "Authorization": SHEETY_API
        }
        self.endpoint = SHEETY_ENDPOINT

    def get_data(self):
        res = requests.get(url=self.endpoint,headers=self.header)
        res.raise_for_status()
        self.data = [ (result['city'], result['iataCode'], result['lowestPrice'], result['id']) for result in res.json()['arkusz1']]
        return self.data
    
    def save_lower_price(self,row, link):
        put_endpoint = f'{self.endpoint}/{row}'
        json={
            'arkusz1':{
                'offer':link
            }
        }
        req = requests.put(url=put_endpoint,json=json)
        print(req.text)