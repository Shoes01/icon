from typing import Any, Dict, List

from base_state import BaseState
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text

class TaskPickerScreen(BaseState):
    def __init__(self, team: Team, tasks: List[Task]):
        self.team = team
        self.tasks = tasks
        menu_title = "Please choose a task."

        menu_options = []
        for task in self.tasks:
            if task.category == team.category:
                menu_options.append(task)

        super().__init__(menu_title=menu_title, menu_options=menu_options, name="TaskPickerScreen")


    def render(self) -> None:
        print_important_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.name}\n"
        print_regular_text(text)
        print_regular_text("n. Cycle display.")


    def handle_input(self, user_input: int) -> Dict[str, Any]:
        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                chosen_task = self.menu_options[input_as_int-1]
                chosen_task.assigned_team_id = self.team.id
                chosen_task.state = TaskState.QUEUED
                self.team.state = TeamState.WORKING

        return {"all_done": True}