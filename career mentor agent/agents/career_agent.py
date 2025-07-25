class CareerAgent:
    def run(self, data=None):
        print("👩‍🎓 CareerAgent: Let's find the best field for you!")
        user_input = input("Enter your interest (e.g. tech, art, medicine): ")
        suggested_field = self.suggest_field(user_input)
        print(f"Suggested field: {suggested_field}")
        return {
            "next_agent": "SkillAgent",
            "data": {"field": suggested_field}
        }

    def suggest_field(self, interest):
        mapping = {
            "tech": "Software Engineering",
            "art": "Graphic Design",
            "medicine": "Nursing"
        }
        return mapping.get(interest.lower(), "Business Management")
