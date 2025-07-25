import chainlit as cl
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent
from tools.roll_dice import roll_dice
from tools.generate_event import generate_event

narrator = NarratorAgent()
monster = MonsterAgent()
item = ItemAgent()

@cl.on_message
async def on_message(message: cl.Message):
    await cl.Message(content="🎮 Welcome, brave warrior! Let's begin your quest...").send()

    # Narrator triggers event
    event = generate_event()
    await cl.Message(content=f"📖 **Narrator**: {event}").send()

    if "monster" in event.lower() or "spider" in event.lower():
        result = roll_dice()
        await cl.Message(content=f"👹 **Monster** attacks! You rolled a {result}").send()

        if result >= 4:
            await cl.Message(content="✅ You defeated the monster!").send()
        else:
            await cl.Message(content="💀 The monster hit you! You barely survived.").send()

    # Item reward
    found_item = item.get_item()
    await cl.Message(content=f"🎁 You found: **{found_item}**").send()

    await cl.Message(content="🏁 The journey ends here... for now.").send()
