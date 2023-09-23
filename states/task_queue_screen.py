from typing import List, Dict, Any

from base_state import BaseState
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_color

title = "Task Queue"

class TaskQueueScreen(BaseState):
    def __init__(self, tasks: List[Task], teams: List[Team]):
        super().__init__(menu_title=title, menu_options=tasks, name="TaskQueueScreen")
        self.tasks = tasks
        self.teams = teams
    
    # Print a list of tasks, and the assigned team.
    ## I will need to track this, I guess, eh.
    # Input will change the QUEUED state of a task to AVAILABLE.
    ## It will also be removed from the list. 

    def render(self):
        print_important_text(self.menu_title)
        print_regular_text("Choose a task to remove from the queue.")
        i = 1
        for task in self.tasks:
            if task.state == TaskState.QUEUED:
                assigned_team = None
                for team in self.teams:
                    if team.id == task.assigned_team_id:
                        assigned_team = team
                        break
                else:
                    print("ERROR: No team assigned to task.")
                print_regular_text(f"{i}. {task.name} - {task.category.upper()} - {assigned_team.name}[{assigned_team.id}]")
    
    def handle_input(self, user_input: int) -> Dict[str, Any]:
        task_to_remove = self.tasks[user_input-1]
        print(f"Task to remove: {task_to_remove.name}")
        print(f"Task's team-assigned's ID: {task_to_remove.assigned_team_id}")
        team_to_remove = None
        for team in self.teams:
            if team.id == task_to_remove.assigned_team_id:
                team_to_remove = team
                task_to_remove.state = TaskState.AVAILABLE
                team_to_remove.state = TeamState.AVAILABLE
                return {"make_task_available": True}
        return {"failed_to_remove_task": False}