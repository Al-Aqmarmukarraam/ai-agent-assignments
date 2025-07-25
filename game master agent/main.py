from agent_runner_mock import AgentRunner
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent
from tools.roll_dice import roll_dice
from tools.generate_event import generate_event

if __name__ == "__main__":
    runner = AgentRunner()

    # Register tools
    runner.register_tool("roll_dice", roll_dice)
    runner.register_tool("generate_event", generate_event)

    # Register agents
    runner.register_agent("NarratorAgent", NarratorAgent())
    runner.register_agent("MonsterAgent", MonsterAgent())
    runner.register_agent("ItemAgent", ItemAgent())

    print("🎮 Welcome to Fantasy Adventure Game!")
    runner.run("NarratorAgent")
