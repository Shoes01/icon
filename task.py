from typing import List

from icon import Icon, icon_factory

class Task:
    def __init__(self, name: str, description: str, category: str, icons: List[Icon]):
        self.name = name
        self.description = description
        self.category = category
        self.icons = icons

        self.is_complete = False


def task_factory(task: str) -> Task:
    match task:
        #
        # XCOM
        #
        case "xcom_1":
            return Task(
                name="XCOM Task",
                description="This is a EXTRATERRESTRIALS COMMAND task.",
                category="xcom",
                icons=[icon_factory("attack")]
            )
        #
        # SIGINT
        #
        case "sigint_1":
            return Task(
                name="SIGINT Task", 
                description="This is a SIGNALS INTELLIGENCE task.", 
                category="sigint",
                icons=[icon_factory("analysis"), icon_factory("analysis"), icon_factory("observation")]
            )
        case "sigint_2":
            return Task(
                name="SIGINT Task 2",
                description="This is a SIGNALS INTELLIGENCE task (2).",
                category="sigint",
                icons=[icon_factory("observation")]
            )
        #
        # SATCOM
        #