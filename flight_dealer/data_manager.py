from dotenv import load_dotenv
import os
import requests

load_dotenv()

class DataManager:
    def __init__(self):
        self._jwt_token = os.getenv("SHEETY_TOKEN")
        self._sheety_url = os.getenv("SHEETY_ENDPOINT")
        self._headers = {"Authorization": f"Bearer {self._jwt_token}"}
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(url=self._sheety_url, headers=self._headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data.get("prices", [])
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self._sheety_url}/{city['id']}",
                json=new_data,
                headers=self._headers
            )
            if response.status_code == 200:
                print(f"✅ Updated {city['city']} with IATA {city['iataCode']}")
            else:
                print(f"❌ Failed to update {city['city']}: {response.text}")
