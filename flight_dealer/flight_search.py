from dotenv import load_dotenv
import os
import requests

load_dotenv()

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("FLIGHT_API")
        self._api_secret = os.getenv("FLIGHT_SECRET")
        self._get_token_endpoint = os.getenv("FLIGHT_TOKEN_ENDPOINT")
        self._flight_search_city_endpoint = os.getenv("FLIGHT_SEARCH_CITY_ENDPOINT")
        self._flight_search_offers = os.getenv("FLIGHT_SEARCH_ENDPOINT")
        self._token = self._get_new_token()

    def _get_new_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=self._get_token_endpoint, headers=headers, data=body)
        response.raise_for_status()
        return response.json()["access_token"]

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {"keyword": city_name, "max": "2", "include": "AIRPORTS"}
        response = requests.get(url=self._flight_search_city_endpoint, headers=headers, params=query)

        if response.status_code != 200:
            print(f"❌ Failed to fetch IATA for {city_name}: {response.text}")
            return "N/A"

        data = response.json().get("data", [])
        if not data:
            print(f"⚠️ No IATA code found for {city_name}")
            return "N/A"

        return data[0].get("iataCode", "N/A")

    def get_flight_offers(self, origin_city_code, destination_city_code, from_time, to_time=None):
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "false",
            "currencyCode": "GBP",
            "max": "10"
        }

        # Only add return date if specified
        if to_time:
            query["returnDate"] = to_time.strftime("%Y-%m-%d")

        response = requests.get(url=self._flight_search_offers, headers=headers, params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("❌ There was a problem with the flight search.")
            print("Response body:", response.text)
            return None

        return response.json()
