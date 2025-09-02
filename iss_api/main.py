import requests
from datetime import datetime

MY_LAT = 59.075983
MY_LONG = 52.877655

def is_iss_near():
  response = requests.get(url="http://api.open-notify.org/iss-now.json#")
  response.raise_for_status()
  data = response.json()["iss_position"]
  iss_longitude = float(data["longitude"])
  iss_latitude = float(data["latitude"])

  if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
    return True
  else:
    return False

def is_night():

  parameters  = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
  }

  response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
  response.raise_for_status()
  data = response.json()
  sunrise = int(data["results"]["sunrise"].split(":")[0])
  sunset = int(data["results"]["sunset"].split(":")[0])

  time_now = datetime.now()
  hour = time_now.strftime("%I").lstrip("0")  # Remove leading zero
  minute_second = time_now.strftime(":%M:%S %p")
  time_12hr = hour + minute_second

  time_now_formatted = int(time_12hr.split(":")[0])

  if time_now_formatted >= sunset or time_now_formatted <= sunrise:
    return True

if is_iss_near() and is_night():
  pass

