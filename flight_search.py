import datetime as dt
import requests
import os
from dotenv import load_dotenv
from flight_data import FlightData

load_dotenv()
KIWI_API = os.environ.get('KIWI_API')
KIWI_ENDPOINT = os.environ.get('KIWI_ENDPOINT')

today=dt.datetime.now().strftime('%d/%m/%Y')
date_to = (dt.datetime.now()+dt.timedelta(days=10)).strftime('%d/%m/%Y')

class FlightSearch:
    def __init__(self,fly_to,price):
        self.is_found=False
        self.price=price
        self.headers={
            'apikey':KIWI_API,
        }
        self.params={ 
            'fly_from':'PL',
            'fly_to':fly_to,
            'date_from':today,
            'date_to':date_to,
            "nights_in_dst_from": 3,
            "nights_in_dst_to": 21,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            'price_to':self.price
        }

    def get_flights(self):
        res = requests.get(url=KIWI_ENDPOINT,params=self.params,headers=self.headers)
        res.raise_for_status()
        #data = [(result['local_departure'],result['price']) for result in res.json()['data']]
        data=res.json()['data']
        if len(data) > 0:
            self.is_found=True
            cheapest_flight = data[0] 
            #print(cheapest_flight)
            self.flight_data = FlightData(
                price=cheapest_flight["price"],
                origin_city=cheapest_flight["route"][0]["cityFrom"],
                origin_airport=cheapest_flight["route"][0]["flyFrom"],
                destination_city=cheapest_flight["route"][0]["cityTo"],
                destination_airport=cheapest_flight["route"][0]["flyTo"],
                out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
                return_date=cheapest_flight["route"][1]["local_departure"].split("T")[0],
                link=cheapest_flight['deep_link']
            )
            # self.flight_data = {'city_from':cheapest_flight['cityFrom'],
            #                     'airport_from':cheapest_flight['flyFrom'],
            #                     'city_to':cheapest_flight['cityTo'],
            #                     'airport_to':cheapest_flight['flyTo'],
            #                     'price':cheapest_flight['price'],
            #                     'departure':cheapest_flight['local_departure'],
            #                     'link':cheapest_flight['deep_link']}
    
    # def check_prices(self):
    #     self.data=self.get_data()
    #     for flight in self.data:
    #         if flight[1] < self.price:
    #             print('price alert!')
    #             return True
    #     return False

# f=FlightSearch('PAR',100)
# f.get_flights()