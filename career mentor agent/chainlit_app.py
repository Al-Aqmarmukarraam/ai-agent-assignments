import chainlit as cl
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

career_agent = CareerAgent()
skill_agent = SkillAgent()
job_agent = JobAgent()

@cl.on_message
async def on_message(message: cl.Message):
    interest = message.content
    field = career_agent.suggest_field(interest)
    skills = skill_agent.run({"data": {"field": field}})["data"]["skills"]
    job_agent.run({"data": {"field": field, "skills": skills}})
    await cl.Message(content=f"Career: {field}\n\nSkills:\n- " + "\n- ".join(skills)).send()
