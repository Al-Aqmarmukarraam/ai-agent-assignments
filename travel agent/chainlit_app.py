import chainlit as cl
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

destination_agent = DestinationAgent()
booking_agent = BookingAgent()
explore_agent = ExploreAgent()

@cl.on_message
async def on_message(message: cl.Message):
    mood = message.content
    dest = destination_agent.suggest_destination(mood)

    await cl.Message(content=f"📍 Suggested Destination: **{dest}**").send()

    flights = booking_agent.get_flights(dest)
    hotels = booking_agent.get_hotels(dest)

    await cl.Message(content=f"✈️ Flights:\n- " + "\n- ".join(flights)).send()
    await cl.Message(content=f"🏨 Hotels:\n- " + "\n- ".join(hotels)).send()

    tips = explore_agent.get_explore_tips(dest)
    await cl.Message(content=f"🗺 Things to Explore in {dest}:\n- " + "\n- ".join(tips)).send()
