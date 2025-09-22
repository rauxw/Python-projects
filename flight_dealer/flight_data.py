class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
    if data is None or not data.get("data"):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

    cheapest_flight = None
    lowest_price = float("inf")

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        itineraries = flight["itineraries"]

        # Outbound info
        nr_stops = len(flight[0]["itineraries"][0]["segments"]) - 1
        origin = itineraries[0]["segments"][0]["departure"]["iataCode"]
        destination = itineraries[0]["segments"][0]["arrival"]["iataCode"]
        out_date = itineraries[0]["segments"][0]["departure"]["at"].split("T")[0]

        # Return info (if exists)
        if len(itineraries) > 1:
            return_date = itineraries[1]["segments"][0]["departure"]["at"].split("T")[0]
        else:
            return_date = "N/A"

        # Compare prices
        if price < lowest_price:
            lowest_price = price
            cheapest_flight = FlightData(price, origin, destination, out_date, return_date, nr_stops)

    if cheapest_flight:
        print(f"Cheapest flight: {cheapest_flight.origin_airport} → {cheapest_flight.destination_airport} "
              f"for £{cheapest_flight.price} (Depart: {cheapest_flight.out_date}, Return: {cheapest_flight.return_date})")
    else:
        print("No valid flights found")
        cheapest_flight = FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    return cheapest_flight
