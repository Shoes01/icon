from typing import Any, Dict, List

from states.base_state import BaseState
from task import Task, TaskState, TaskSubcategory
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_color

class TeamPickerScreen(BaseState):
    def __init__(self, task: Task, teams: List[Team]):
        self.task = task
        self.teams = teams
        menu_title = "Please choose a team."

        menu_options = []
        for team in self.teams:
            if team.category == task.category:
                menu_options.append(team)

        self.available_teams = [team for team in self.teams if team.state == TeamState.AVAILABLE]
        self.unavailable_teams = [team for team in self.teams if team.state != TeamState.AVAILABLE]

        super().__init__(menu_title=menu_title, menu_options=self.available_teams, name="TeamPickerScreen")


    def render(self) -> None:
        print_important_text(self.menu_title)
        text = ""
        # TODO: need to print in yellow the teams that can't.
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.name}\n"
        print_regular_text(text)

        # print unavailable teams/tasks
        text = ""
        for team in self.unavailable_teams:
            text += f"   {team.name}\n"
        print_color(text=text, fore="yellow", back="black", end="")
        

    def handle_input(self, user_input: int) -> Dict[str, Any]:
        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                chosen_team: Team = self.menu_options[input_as_int-1]
                match self.task.subcategory:
                    case TaskSubcategory.SUPPORT:
                        return {"need to pick team a to support": (self.task, chosen_team)}
                    case TaskSubcategory.PASSIVE:
                        chosen_team.working_on_task = self.task.id
                        self.task.state = TaskState.QUEUED
                        chosen_team.state = TeamState.WORKING
                    case TaskSubcategory.ACTIVE:
                        # TODO: need event code.
                        pass



        return {"all_done": True}