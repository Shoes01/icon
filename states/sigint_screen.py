from typing import List, Dict, Any

from base_state import BaseState
from task import Task
from team import Team
from print_color import print_regular_text, print_important_text, print_VIP_text


title = "Welcome to SIGNALS INTELLIGENCE"


class SigintScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team]):
        super().__init__(menu_title=title, menu_options=tasks)
        self.teams: List[Team] = teams
        self.chosen_task: Task = None
        self.chosen_team: Team = None
        self.on_menu: str = "one"
    

    def render(self):
        # Pick a task.
        if self.on_menu == "one":
            print_important_text(self.menu_title)
            if len(self.menu_options) == 0:
                print_VIP_text("There are no tasks.")
                return
            print_regular_text("Tasks:")
            for i, option in enumerate(self.menu_options):
                print_regular_text(f"  {i+1}. {option.name}")
        # Pick a team.
        if self.on_menu == "two":
            print_important_text("Which team do you want to assign to this task?")
            print_regular_text("Teams:")
            if len(self.teams) == 0:
                print_VIP_text("There are no teams.")
                return
            for i, team in enumerate(self.teams):
                print_regular_text(f"  {i+1}. {team.name}")


    def handle_input(self, user_input: int) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        if self.chosen_task is None:
            self.chosen_task = self.menu_options[user_input-1]
            self.on_menu = "two"
            result["chose a task, now waiting for a team."] = False
        else:
            self.chosen_team = self.teams[user_input-1]
            result["task"] = (self.chosen_task, self.chosen_team)
        
        return result