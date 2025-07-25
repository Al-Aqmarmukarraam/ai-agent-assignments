class JobAgent:
    def run(self, input):
        field = input["data"]["field"]
        print(f"💼 JobAgent: Here are some jobs in {field}...")
        jobs = self.get_jobs(field)
        print("- " + "\n- ".join(jobs))
        return {"done": True}

    def get_jobs(self, field):
        job_data = {
            "Software Engineering": ["Frontend Developer", "Backend Developer", "DevOps Engineer"],
            "Graphic Design": ["UI Designer", "Logo Designer", "Creative Director"],
            "Nursing": ["Registered Nurse", "Clinical Nurse", "Surgical Assistant"],
            "Business Management": ["Operations Manager", "HR Executive", "Project Coordinator"]
        }
        return job_data.get(field, ["General Associate"])
