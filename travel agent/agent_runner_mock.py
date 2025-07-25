class AgentRunner:
    def __init__(self):
        self.agents = {}
        self.tools = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent

    def register_tool(self, name, func):
        self.tools[name] = func

    def run(self, start_agent):
        current = start_agent
        data = None
        while True:
            agent = self.agents[current]
            result = agent.run(data)
            if result.get("done"):
                break
            current = result["next_agent"]
            data = result
