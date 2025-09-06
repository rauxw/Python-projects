import os
from dotenv import load_dotenv

load_dotenv()

import requests
from twilio.rest import Client

LATITUDE=os.getenv('LATITUDE')
LONGITUDE=os.getenv('LONGITUDE')

OWN_ENDPOINT = os.getenv('OWN_ENDPOINT')
API_KEY = os.getenv('API_KEY')

# twilio api
ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

parameters = {
  "lat":LATITUDE,
  "lon":LONGITUDE,
  "cnt":"4",
  "appid":API_KEY
}

response = requests.get(OWN_ENDPOINT, params=parameters)

response.raise_for_status()

status = response.status_code

weather = response.json()

will_rain = False

for i in range(0,4):
  weather_code = int(weather["list"][i]["weather"][0]["id"])

  if weather_code < 700:
    will_rain = True

client = Client(ACCOUNT_SID, AUTH_TOKEN)

if will_rain:
  message = client.messages.create(
    body="It's going to rain today carry umbrella ☔️",
    from_=os.getenv("FROM_NUMBER"),
    to=os.getenv("TO_NUMBER"),
  )
else:
  message = client.messages.create(
    body="Its not raining today ☀️",
    from_=os.getenv("FROM_NUMBER"),
    to=os.getenv("TO_NUMBER"),
  )

print(message.status)
