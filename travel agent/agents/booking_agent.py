from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

class BookingAgent:
    def run(self, input):
        dest = input["data"]["destination"]
        print(f"✈️ BookingAgent: Finding flights and hotels for {dest}...")
        flights = get_flights(dest)
        hotels = suggest_hotels(dest)
        print("Flights:")
        print("- " + "\n- ".join(flights))
        print("Hotels:")
        print("- " + "\n- ".join(hotels))
        return {
            "next_agent": "ExploreAgent",
            "data": {"destination": dest, "flights": flights, "hotels": hotels}
        }

    # chainlit support
    def get_flights(self, dest):
        return get_flights(dest)

    def get_hotels(self, dest):
        return suggest_hotels(dest)
