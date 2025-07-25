class ItemAgent:
    def run(self, input):
        print("🎁 ItemAgent: You found a mysterious item!")
        item = self.get_item()
        print(f"🧳 Item added to inventory: {item}")

        # End the game after one round for demo
        return {"done": True}

    def get_item(self):
        return "Enchanted Sword"

