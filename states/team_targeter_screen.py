from typing import Any, Dict, List

from states.base_state import BaseState
from team import Team, TeamState
from task import Task, TaskState, TaskSubcategory
from print_color import print_regular_text, print_important_text

class TeamTargeterScreen(BaseState):
    def __init__(self, chosen_team: Team, chosen_task: Task, teams: List[Team]):
        self.chosen_team = chosen_team
        self.chosen_task = chosen_task
        
        menu_title = "Please choose a team to support."
        menu_options = []
        for team in teams:
            if team.id != chosen_team.id:
                menu_options.append(team)

        super().__init__(menu_title=menu_title, menu_options=menu_options, name="TeamTargeterScreen")


    def render(self) -> None:
        print_important_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.name}\n"
        print_regular_text(text)
    

    def handle_input(self, user_input: int) -> Dict[str, Any]:
        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                supported_team: Team = self.menu_options[input_as_int-1]
                self.chosen_team.working_on_task = self.chosen_task.id
                self.chosen_task.state = TaskState.AVAILABLE # The task is always available :) 
                self.chosen_team.state = TeamState.WORKING
                self.chosen_team.supporting_team = supported_team.id
                #supported_team.supported_by_tasks.append(self.chosen_task.id) # This should not be added until it is successfully completed.

        return {"all_done + 1": True}