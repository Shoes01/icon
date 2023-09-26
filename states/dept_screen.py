from typing import List, Dict, Any

from states.base_state import BaseState
from event import Event
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_color


class DeptScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team], events: List[Event], menu_title: str, state_name: str):
        super().__init__(menu_title=menu_title, menu_options=teams, name=state_name)
        self.tasks: List[Task] = tasks
        self.teams: List[Team] = teams
        self.events: List[Event] = events

        self.chosen_task: Task = None
        self.chosen_team: Team = None
        self.display: str = "teams"
    
        self.available_tasks = [task for task in self.tasks if task.state == TaskState.AVAILABLE]
        self.unavailable_tasks = [task for task in self.tasks if task.state != TaskState.AVAILABLE]

        self.available_teams = [team for team in self.teams if team.state == TeamState.AVAILABLE]
        self.unavailable_teams = [team for team in self.teams if team.state != TeamState.AVAILABLE]


    def render(self) -> None:
        print_important_text(self.menu_title)

        if self.display == "teams":
            self.menu_options = self.available_teams
            print_regular_text("Choose a team to assign a task to.")
        elif self.display == "tasks":
            self.menu_options = self.available_tasks
            print_regular_text("Choose a task to assign to a team.")
        
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.name}\n"
        print_regular_text(text, end="")

        # print unavailable teams/tasks
        text = ""
        if self.display == "teams":
            for team in self.unavailable_teams:
                text += f"   {team.name}\n"
        elif self.display == "tasks":
            for task in self.unavailable_tasks:
                text += f"   {task.name}\n"
        print_color(text=text, fore="yellow", back="black", end="")
        print_regular_text("\nn. Cycle display.")


    def handle_input(self, user_input: int) -> Dict[str, Any]:
        result: Dict[str, Any] = {}

        if user_input == "n":
            if self.display == "teams":
                self.display = "tasks"
            elif self.display == "tasks":
                self.display = "teams" 

        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                if self.display == "teams":
                    return {"need a task for this team": self.teams[input_as_int-1]}
                elif self.display == "tasks":
                    return {"need a team for this task": self.tasks[input_as_int-1]}
        
        return result