from typing import Any, Dict, List

from states.base_state import BaseState
from task import Task, TaskState, TaskSubcategory
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_color

class TaskPickerScreen(BaseState):
    def __init__(self, team: Team, tasks: List[Task]):
        self.team = team
        self.tasks = tasks
        menu_title = "Please choose a task."

        category_tasks = []
        for task in self.tasks:
            if task.category == team.category:
                category_tasks.append(task)

        self.available_tasks = [task for task in category_tasks if task.state == TaskState.AVAILABLE]
        self.unavailable_tasks = [task for task in category_tasks if task.state != TaskState.AVAILABLE]

        super().__init__(menu_title=menu_title, menu_options=self.available_tasks, name="TaskPickerScreen")


    def render(self) -> None:
        print_important_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.name}\n"
        print_regular_text(text)

        # Print unavailable tasks.
        text = ""
        for task in self.unavailable_tasks:
            text += f"   {task.name}\n"
        print_color(text=text, fore="yellow", back="black", end="")


    def handle_input(self, user_input: int) -> Dict[str, Any]:
        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                chosen_task: Task = self.menu_options[input_as_int-1]

                match chosen_task.subcategory:
                    case TaskSubcategory.SUPPORT:
                        return {"need to pick team a to support": (chosen_task, self.team)}
                    case TaskSubcategory.PASSIVE:
                        self.team.working_on_task = chosen_task.id
                        chosen_task.state = TaskState.QUEUED
                        self.team.state = TeamState.WORKING
                    case TaskSubcategory.ACTIVE:
                        # TODO: I need more code to handle targeting events.
                        pass


        return {"all_done": True}