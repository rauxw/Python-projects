from dotenv import load_dotenv

load_dotenv()

import os
import requests
import datetime

exercise_endpoint = os.getenv("EXERCISE_ENDPOINT")

exercise_text = input("Which exercise you did:")

headers = {
  "x-app-id": os.getenv("APP_ID"),
  "x-app-key": os.getenv("API_KEY")
}

parameters = {
  "query": exercise_text,
  "gender": os.getenv("GENDER"),
  "weight_kg": os.getenv("WEIGHT_KG"),
  "height_cm": os.getenv("HEIGHT_CM"),
  "age": os.getenv("AGE")
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

sheety_endpoint = os.getenv("SHEETY_ENDPOINT")

for exercise in result['exercises']:
  sheet_inputs = {
    "workout": {
      "date":today_date,
      "time":now_time,
      "exercise": exercise["name"].title(),
      "duration": f"{int(exercise['duration_min'])}min",
      "calories": int(exercise["nf_calories"])
    }
  }

headers = {
  "Authorization": os.getenv("BEARER_TOKEN")
}

sheet_post = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=headers)
print(sheet_post.text)