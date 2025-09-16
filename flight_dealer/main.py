import time
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_mg = NotificationManager()

ORIGIN_CITY_IATA = "LON"


for row in sheet_data:
    if not row['iataCode']:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
        time.sleep(2)

print(f"Sheet data:\n{sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"\nGetting flights for {destination['city']}...")
    flights = flight_search.get_flight_offers(
    ORIGIN_CITY_IATA,
    destination['iataCode'],
    from_time=tomorrow,
    to_time=six_months_from_now
    )

    if not flights or "data" not in flights or not flights["data"]:
        print(f"{destination['city']}: No flights found")
        continue

    cheapest_flight = find_cheapest_flight(flights)

    if cheapest_flight.price != "N/A":
        if cheapest_flight.price < destination["lowestPrice"]:
            notification_mg.send_sms(message_body=f"✅ Deal! {destination['city']}: £{cheapest_flight.price} "
                  f"(threshold {destination['lowestPrice']})")
        else:
            print(f"❌ Too expensive for {destination['city']}: £{cheapest_flight.price} "
                  f"(threshold {destination['lowestPrice']})")
    else:
        print(f"{destination['city']}: No flights found")

    time.sleep(2)

