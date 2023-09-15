from typing import List, Dict, Any

from base_state import BaseState
from task import Task
from team import Team


title = "Welcome to SIGNALS INTELLIGENCE"


class SigintScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team]):
        super().__init__(menu_title=title, menu_options=tasks)
        self.teams = teams
        self.chosen_task: Task = None
        self.chosen_team: Team = None
    
    def render(self):
        print(self.menu_title)
        if len(self.menu_options) == 0:
            print("There are no tasks.")
            return
        print("Tasks:")
        for i, option in enumerate(self.menu_options):
            print(f"{i+1}. {option.name}")


    def render_team_picker(self):
        print("Teams:")
        for i, team in enumerate(self.teams):
            print(f"{i+1}. {team.name}")

    def handle_input(self, user_input: int):
        result: Dict[str, Any] = {}

        self.chosen_task = self.menu_options[user_input-1]
        
        self.render_team_picker()
        user_input = input("Which team do you want to assign to this task? ")
        user_input = self.sanitize_input(user_input)
        if user_input != -1:
            self.chosen_team = self.teams[user_input-1]
            result["task"] = (self.chosen_task, self.chosen_team)
            return result


# CURRENT ISSUE
"""
The list of options for SIGINT will vary.
How will I know what input corresponds to which option?
I could have a generic check for the last option, as it's always "reutrn". Or I can add that to the base state...

I should just return the content of the option ... ?

"""