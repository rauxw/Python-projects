from dotenv import load_dotenv

load_dotenv()

import os
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self._client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))

    def send_sms(self, message_body):
        message = self._client.messages.create(
            body=message_body,
            from_=os.getenv("TWILIO_NUMBER"),
            to=os.getenv("MY_NUMBER"),
        )
        print(message.sid)