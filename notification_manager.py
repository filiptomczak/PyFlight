from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.environ.get('TWILIO_SID')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
TWILIO_FROM = os.environ.get('TWILIO_FROM')
TWILIO_TO = os.environ.get('TWILIO_TO')

class NotificationManager:
    def __init__(self):
        account_sid = TWILIO_SID
        auth_token = TWILIO_TOKEN
        self.client = Client(account_sid, auth_token)

    def send_sms(self,body):
        message = self.client.messages \
                        .create(
                            body=body,
                            from_=TWILIO_FROM,
                            to=TWILIO_TO
                        )