def get_career_roadmap(field):
    roadmaps = {
        "Software Engineering": ["Learn Python", "Understand Data Structures", "Build Projects"],
        "Graphic Design": ["Learn Adobe Suite", "Practice with mockups", "Build Portfolio"],
        "Nursing": ["Study Anatomy", "Do Clinical Practice", "Pass Licensing Exam"],
        "Business Management": ["Learn Business Basics", "Understand Operations", "Manage Teams"]
    }
    return roadmaps.get(field, [])
