class ExploreAgent:
    def run(self, input):
        dest = input["data"]["destination"]
        print(f"🗺 ExploreAgent: Here's what to explore in {dest}...")
        tips = self.get_explore_tips(dest)
        print("- " + "\n- ".join(tips))
        return {"done": True}

    def get_explore_tips(self, destination):
        explore_data = {
            "Bali": ["Visit Ubud", "Enjoy beach sunset", "Try Balinese food"],
            "Nepal": ["Trek to Everest Base Camp", "Visit Kathmandu", "Eat momo"],
            "Rome": ["See the Colosseum", "Eat authentic pasta", "Explore Vatican"],
            "Dubai": ["Visit Burj Khalifa", "Shop in Dubai Mall", "Go dune bashing"]
        }
        return explore_data.get(destination, ["Explore local spots!"])
