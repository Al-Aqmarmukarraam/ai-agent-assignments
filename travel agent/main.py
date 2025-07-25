from agent_runner_mock import AgentRunner
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent
from tools.get_flights import get_flights
from tools.suggest_hotels import suggest_hotels

if __name__ == "__main__":
    runner = AgentRunner()

    # Register tools
    runner.register_tool("get_flights", get_flights)
    runner.register_tool("suggest_hotels", suggest_hotels)

    # Register agents
    runner.register_agent("DestinationAgent", DestinationAgent())
    runner.register_agent("BookingAgent", BookingAgent())
    runner.register_agent("ExploreAgent", ExploreAgent())

    print("🧳 Welcome to AI Travel Designer!")
    runner.run("DestinationAgent")
