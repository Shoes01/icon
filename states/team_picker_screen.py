from typing import Any, Dict, List

from base_state import BaseState
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text

class TeamPickerScreen(BaseState):
    def __init__(self, task: Task, teams: List[Team]):
        self.task = task
        self.teams = teams
        menu_title = "Please choose a team."

        menu_options = []
        for team in self.teams:
            if team.category == task.category:
                menu_options.append(team)

        super().__init__(menu_title=menu_title, menu_options=menu_options, name="TeamPickerScreen")


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
                chosen_team = self.menu_options[input_as_int-1]
                self.task.assigned_team_id = chosen_team.id
                self.task.state = TaskState.QUEUED
                chosen_team.state = TeamState.WORKING

        return {"all_done": True}