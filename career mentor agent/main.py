from agent_runner_mock import AgentRunner
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent
from tools.career_roadmap import get_career_roadmap
from tools.skill_generator import generate_skills

if __name__ == "__main__":
    runner = AgentRunner()

    # Register tools
    runner.register_tool("get_career_roadmap", get_career_roadmap)
    runner.register_tool("generate_skills", generate_skills)

    # Register agents
    runner.register_agent("CareerAgent", CareerAgent())
    runner.register_agent("SkillAgent", SkillAgent())
    runner.register_agent("JobAgent", JobAgent())

    print("🎓 Welcome to Career Mentor AI!")
    runner.run("CareerAgent")

