from dotenv import load_dotenv

load_dotenv()

import os
import requests


class DataManager:
    def __init__(self):
        self._jwt_token = os.getenv("SHEETY_TOKEN")
        self._sheety_url = os.getenv("SHEETY_ENDPOINT")
        self._headers = {"Authorization": "Bearer" + " " + self._jwt_token}
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=self._sheety_url, headers=self._headers)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data= {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self._sheety_url}/{city['id']}",
                json=new_data,
                headers=self._headers
            )
            print(response.text)
