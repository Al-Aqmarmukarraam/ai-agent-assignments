from tools.career_roadmap import get_career_roadmap

class SkillAgent:
    def run(self, input):
        field = input["data"]["field"]
        print(f"📚 SkillAgent: Generating skill roadmap for {field}...")
        skills = get_career_roadmap(field)
        print("Skills Required:")
        print("- " + "\n- ".join(skills))
        return {
            "next_agent": "JobAgent",
            "data": {"field": field, "skills": skills}
        }
