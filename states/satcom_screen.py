from typing import List, Dict, Any

from base_state import BaseState
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_two_columns, print_text_error


title = "Welcome to SATELLITE COMMAND"


class SatcomScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team]):
        super().__init__(menu_title=title, menu_options=teams, name="SatcomScreen")
        self.tasks: List[Task] = tasks
        self.teams: List[Team] = teams
        self.chosen_task: Task = None
        self.chosen_team: Team = None
        self.on_menu: str = "one"
    

    def render(self):
        print_important_text(self.menu_title)
        prompt = "Choose a team." if self.on_menu == "one" else "Choose a task."
        print_regular_text(prompt)
        print_two_columns(self.teams, self.tasks)


    def handle_input(self, user_input: int) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        # Need extra safety checks for user input.
        if self.on_menu == "one" and (user_input < 1 or user_input > len(self.teams)):
            print_text_error(f"Invalid choice ({user_input=}). Please enter a number between 1 and ", len(self.teams))
            return result
        if self.on_menu == "two" and (user_input < 1 or user_input > len(self.tasks)):
            print_text_error(f"Invalid choice ({user_input=}). Please enter a number between 1 and ", len(self.tasks))
            return result

        if self.chosen_team is None:
            if self.teams[user_input-1].state != TeamState.AVAILABLE:
                print_text_error("This team is assigned to a task already.")
                return result
            self.chosen_team = self.teams[user_input-1]
            self.chosen_team.state = TeamState.CHOSEN
            self.on_menu = "two"
            result["chose a team, now waiting for a task."] = False
        else:
            if self.tasks[user_input-1].state != TaskState.AVAILABLE:
                print_text_error("This task is assigned to a team already.")
                return result
            self.chosen_task = self.tasks[user_input-1]
            self.chosen_team.state = TeamState.WORKING
            self.chosen_task.state = TaskState.QUEUED
            self.chosen_task.assigned_team_id = self.chosen_team.id
            result["task_assigned"] = True
        
        return result