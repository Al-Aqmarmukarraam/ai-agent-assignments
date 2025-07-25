import random

def generate_event():
    events = [
        "You hear growling... a monster appears!",
        "You find a shiny chest in the shadows.",
        "A path splits into two: left or right?",
        "A giant spider blocks your way!",
        "You stumble on an old map."
    ]
    return random.choice(events)
