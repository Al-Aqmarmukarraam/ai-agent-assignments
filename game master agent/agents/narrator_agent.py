from tools.generate_event import generate_event

class NarratorAgent:
    def run(self, input=None):
        print("📖 NarratorAgent: Your journey begins in a dark forest...")
        event = generate_event()
        print(f"📜 Event: {event}")

        if "monster" in event.lower():
            return {
                "next_agent": "MonsterAgent",
                "data": {"event": event}
            }
        else:
            return {
                "next_agent": "ItemAgent",
                "data": {"event": event}
            }
