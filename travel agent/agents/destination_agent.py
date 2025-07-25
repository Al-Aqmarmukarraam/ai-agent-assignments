class DestinationAgent:
    def run(self, input=None):
        print("📍 DestinationAgent: Let's choose a destination!")
        mood = input("What's your travel mood? (relax/adventure/culture): ")
        destination = self.suggest_destination(mood)
        print(f"Suggested destination: {destination}")
        return {
            "next_agent": "BookingAgent",
            "data": {"destination": destination}
        }

    def suggest_destination(self, mood):
        mapping = {
            "relax": "Bali",
            "adventure": "Nepal",
            "culture": "Rome"
        }
        return mapping.get(mood.lower(), "Dubai")
