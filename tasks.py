from icons import Icon
from typing import List


class Task:
    # A task is completed by a team belonging to the player.
    # The combat engine takes care of resolving the task. 
    # It is essentially a collection of icons, and some metadata.
    def __init__(self, icons: List, name: str, category: str):
        self.icons = icons
        self.name = name
        self.category = category


def task_factory(type: str) -> Task:
    if type == "test":
        icons = [Icon("A"), Icon("D")]
        name = "Test Task"
        category = "attack"
        return Task(icons, name, category)
    else:
        print(f"Task {type} is invalid")