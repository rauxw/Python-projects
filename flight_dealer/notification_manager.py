from dotenv import load_dotenv

load_dotenv()

import os
from twilio.rest import Client
import smtplib


class NotificationManager:
    def __init__(self):
        self.smtp_address = os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS")
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_EMAIL_PASSWORD")
        self.twilio_virtual_number = os.getenv("TWILIO_NUMBER")
        self.my_number = os.getenv("MY_NUMBER")
        self._client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        self.connection = smtplib.SMTP(os.getenv("EMAIL_PROVIDER_SMTP_ADDRESS"))

    def send_sms(self, message_body):
        message = self._client.messages.create(
            body=message_body,
            from_=os.getenv("TWILIO_NUMBER"),
            to=os.getenv("MY_NUMBER"),
        )
        print(message.sid)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )