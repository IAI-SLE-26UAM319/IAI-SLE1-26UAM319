
# Smart Vacuum Cleaner Agent
# SLE-1: Introduction to Artificial Intelligence

class VacuumAgent:
    def __init__(self, environment, location):
        self.environment = environment
        self.location = location

    def perceive(self):
        return self.environment[self.location]

    def act(self):
        if self.perceive() == "Dirty":
            print("Location", self.location, "is dirty.")
            print("Action: Cleaning...")
            self.environment[self.location] = "Clean"

        else:
            print("Location", self.location, "is clean.")

            if self.location == "A":
                print("Action: Moving to B")
                self.location = "B"
            else:
                print("Action: Moving to A")
                self.location = "A"

    def run(self):
        print("Starting Smart Vacuum Cleaner Agent")

        while True:
            print("\nCurrent Location:", self.location)
            self.act()

            if all(status == "Clean"
                   for status in self.environment.values()):
                print("\nBoth locations are clean!")
                print("Agent completed its task.")
                break


# Create the environment
environment = {
    "A": "Dirty",
    "B": "Dirty"
}

# Create the agent
agent = VacuumAgent(environment, "A")

# Run the agent
agent.run()
