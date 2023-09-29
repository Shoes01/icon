from typing import List, Dict, Any

from states.base_state import BaseState
from task import Task, TaskState, TaskSubcategory
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_color

title = "Task Queue"

class TaskQueueScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team]):
        self.teams = teams
        self.tasks = tasks

        menu_options: List[Team] = []
        for team in teams:
            if team.working_on_task >= 0:
                menu_options.append(team)

        super().__init__(menu_title=title, menu_options=menu_options, name="TaskQueueScreen")
    

    def render(self):
        print_important_text(self.menu_title)
        print_regular_text("Recall a team from their task.")
        i = 1
        for team in self.menu_options:
            assigned_team: Team = None
            is_ongoing = ""
            for task in self.tasks:
                if team.working_on_task == task.id:
                    assigned_team = team
                    is_ongoing = "[SUPPORTING]" if task.subcategory == TaskSubcategory.SUPPORT else ""
                    break
            else:
                print("ERROR: No team assigned to task.")
            

            print_regular_text(f"{i}. {assigned_team.name} - {task.name} - {task.category.upper()}{is_ongoing}")
    

    def handle_input(self, user_input: int) -> Dict[str, Any]:
        if user_input.isdigit():
            input_as_int = int(user_input)
            if input_as_int > 0 and input_as_int <= len(self.menu_options):
                team_to_remove: Team = self.menu_options[input_as_int-1]
                task_to_remove = None
                for task in self.tasks:
                    if team_to_remove.working_on_task == task.id:
                        task_to_remove = task
                        task_to_remove.state = TaskState.AVAILABLE
                        team_to_remove.state = TeamState.AVAILABLE
                        team_to_remove.working_on_task = -1
                        if team_to_remove.cooldown > 0:
                            team_to_remove.state = TeamState.COOLDOWN
                        self.menu_options.remove(team_to_remove)
                        return {"make_task_available": True}
                return {"failed_to_remove_task": False}
        return {"invalid input": False}