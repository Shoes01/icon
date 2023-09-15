class Task:
    def __init__(self, name, description, category, when_completed, when_failed):
        self.name = name
        self.description = description
        self.category = category
        self.when_completed = when_completed
        self.when_failed = when_failed

        self.is_complete = False

def task_factory(task: str) -> Task:
    match task:
        case "sigint_1":
            return Task(
                name="SIGINT Task", 
                description="This is a SIGNALS INTELLIGENCE task.", 
                category="sigint",
                when_completed="sigint_2",
                when_failed="sigint_1")