#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


notification_manager=NotificationManager()
data_manager=DataManager()
iatas_prices = data_manager.get_data()

for item in iatas_prices:
    print(f'looking for flight to: {item[0]}')
    flight = FlightSearch(fly_to = item[1], price = item[2])
    flight.get_flights()
    if flight.is_found:
        data_manager.save_lower_price(row=item[3],link=flight.flight_data.link)
        body = f'PRICE ALERT flight to {flight.flight_data.destination_city} from {flight.flight_data.origin_airport} for {flight.flight_data.price} EUR, {flight.flight_data.out_date}-{flight.flight_data.return_date}'
        notification_manager.send_sms(body)