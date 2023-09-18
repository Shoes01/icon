from typing import List
from enum import Enum

from icon import Icon, icon_factory


class TaskState(Enum):
    AVAILABLE = 1
    IN_PROGRESS = 2
    SUCCESSFUL = 3
    UNSUCCESSFUL = 4


class Task:
    def __init__(self, name: str, description: str, category: str, icons: List[Icon], wincon: int, losecon: int):
        self.name = name
        self.description = description
        self.category = category
        self.icons = icons
        self.wincon = wincon
        self.losecon = losecon

        self.state = TaskState.AVAILABLE


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
                icons=[icon_factory("attack")],
                wincon=6,
                losecon=4,
            )
        #
        # SIGINT
        #
        case "sigint_1":
            return Task(
                name="SIGINT Task", 
                description="SIGINT is initiating analysis: Scouring the airwaves for alien signals...", 
                category="sigint",
                icons=[icon_factory("analysis"), icon_factory("analysis"), icon_factory("observation")],
                wincon=6,
                losecon=4,
            )
        case "sigint_2":
            return Task(
                name="SIGINT Task 2",
                description="This is a SIGNALS INTELLIGENCE task (2).",
                category="sigint",
                icons=[icon_factory("observation")],
                wincon=6,
                losecon=4,
            )
        #
        # SATCOM
        #