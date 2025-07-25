from tools.roll_dice import roll_dice

class MonsterAgent:
    def run(self, input):
        print("👹 MonsterAgent: A wild monster appears!")
        result = roll_dice()
        print(f"🎲 You rolled a {result}!")

        if result >= 4:
            print("✅ You defeated the monster!")
        else:
            print("💀 The monster hit you! You barely survived.")

        return {
            "next_agent": "ItemAgent",
            "data": input  # pass original event forward
        }
