from typing import List, Dict, Any
import os

from states.base_state import BaseState
from states.root_menu import RootMenu
from states.main_screen import MainScreen
from states.satcom_screen import SatcomScreen
from states.sigint_screen import SigintScreen
from states.task_queue_screen import TaskQueueScreen
from states.team_picker_screen import TeamPickerScreen
from states.task_picker_screen import TaskPickerScreen
from states.team_targeter_screen import TeamTargeterScreen
from event import Event
from task import Task, task_factory, TaskState, TaskSubcategory
from team import Team, team_factory, TeamState
from combat import do_combat
from print_color import print_regular_text, print_text_input, print_important_text
from debug_options import DEBUG_ALWAYS_CLEAR_TEMRINAL, DEBUG_ALWAYS_PRINT_STATE


class Game:
    def __init__(self):
        self.running = True
        self.state_stack: List[BaseState] = [RootMenu(),]
        self.turn_count: int = 0
        self.tasks: List[Task] = []
        self.teams: List[Team] = []
        self.events: List[Event] = []

        self.add_team(team_factory("sigint"))
        self.add_team(team_factory("sigint"))
        self.add_team(team_factory("satcom"))
        self.add_team(team_factory("xcom"))
        self.alerts: Dict[str, int] = {"sigint": 0, "satcom": 0, "xcom": 0}

        self.tasks.append(task_factory("real_time_comms"))

    def push_state(self, state: BaseState):
        self.state_stack.append(state)
    

    def pop_state(self):
        if len(self.state_stack) == 1:
            self.quit()
        else:
            self.state_stack.pop()


    def run(self):
        while self.running:
            if DEBUG_ALWAYS_PRINT_STATE: print(f"DEBUG: {self.state_stack[-1].name=}")
            if DEBUG_ALWAYS_CLEAR_TEMRINAL:
                os.system('cls' if os.name == 'nt' else 'clear')
            self.state_stack[-1].render()
            
            if self.state_stack[-1].name != "MainScreen" and self.state_stack[-1].name != "RootMenu":
                print_regular_text("b. Back\n")
            else:
                print()

            print_text_input(f"[TURN {self.turn_count:3d}]> ")
            user_input: str = input().lower()
            print("\n")

            user_input = self.handle_input(user_input)
            result = self.state_stack[-1].handle_input(user_input)
            if result: 
                self.update(result)


    def handle_input(self, user_input) -> str:
        match user_input:
            case "x": 
                self.quit()
                user_input = ""
            case "b":
                if self.state_stack[-1].name == "RootMenu":
                    self.quit()
                    return user_input
                elif self.state_stack[-1].name == "MainScreen":
                    return user_input
                self.pop_state()
                for team in self.teams:
                    if team.state == TeamState.CHOSEN:
                        team.state = TeamState.AVAILABLE
                user_input = ""
        return user_input


    def end_turn(self):
        # Prepare combat.
        for team in self.teams:
            for task in self.tasks:
                if team.working_on_task == task.id and team.state != TeamState.SUPPORTING:
                    do_combat(team, task, self.teams, self.tasks)
        # Iterate cooldown.
        for team in self.teams:
            if team.cooldown > 0 and team.state != TeamState.SUPPORTING:
                team.cooldown -= 1
            if team.cooldown == 0 and team.state == TeamState.COOLDOWN:
                team.state = TeamState.AVAILABLE
            
        print_important_text(f"Turn {self.turn_count} complete.\n")
        self.turn_count += 1
        for key in self.alerts:
            self.alerts[key] = 0
        self.update_tasks()


    def quit(self):
        self.running = False
    

    def update(self, update: Dict[str, Any]):
        for key, value in update.items():
            match key:
                case "new_game":
                    self.state_stack.append(MainScreen(self.alerts, self.tasks, self.teams))
                case "quit":
                    self.quit()
                case "end_turn":
                    self.end_turn()
                case "satcom":
                    tasks: List[Task] = self.get_tasks("satcom")
                    teams: List[Team] = self.get_teams("satcom")
                    self.state_stack.append(SatcomScreen(tasks=tasks, teams=teams, events=[]))
                case "sigint":
                    tasks: List[Task] = self.get_tasks("sigint")
                    teams: List[Team] = self.get_teams("sigint")
                    self.state_stack.append(SigintScreen(tasks=tasks, teams=teams, events=[]))
                case "task_queue":
                    self.state_stack.append(TaskQueueScreen(tasks=self.tasks, teams=self.teams))
                case "task_assigned":
                    self.pop_state()
                case "all_done":
                    self.pop_state()
                    self.pop_state() # This takes us all the way back to the main screen.
                case "all_done + 1":
                    self.pop_state()
                    self.pop_state()
                    self.pop_state() # This takes us all the way back to the main screen.
                case "need a team for this task":
                    # TODO: What is in this value? It seems to be a single task.
                    task: Task = value
                    self.state_stack.append(TeamPickerScreen(task=task, teams=self.teams))
                case "need a task for this team":
                    team: Team = value
                    self.state_stack.append(TaskPickerScreen(team=team, tasks=self.tasks))
                case "need to pick team a to support":
                    task: Task = value[0]
                    team: Team = value[1]
                    self.state_stack.append(TeamTargeterScreen(chosen_team=team, chosen_task=task, teams=self.teams))


    def add_team(self, team: Team):
        self.teams.append(team)
    

    def get_teams(self, category: str) -> List[Team]:
        results: List[Team] = []
        for team in self.teams:
            if team.category == category:
                results.append(team)
        return results


    def add_task(self, task: Task):
        self.tasks.append(task)
        self.alerts[task.category] += 1


    def remove_task(self, task: Task):
        self.tasks.remove(task)


    def get_tasks(self, category: str) -> List[Task]:
        results: List[Task] = []
        for task in self.tasks:
            if task.category == category:
                results.append(task)
        return results


    def update_tasks(self):
        if self.turn_count == 1:
            self.add_task(task_factory("sigint_1"))
            self.add_task(task_factory("satcom_1"))
            self.add_task(task_factory("satcom_1"))
        
        for task in self.tasks:
            match task.state:
                case TaskState.SUCCESSFUL:
                    for task_codename in task.win_tasks:
                        self.add_task(task_factory(task_codename))
                    if task.subcategory != TaskSubcategory.SUPPORT:
                        self.remove_task(task)
                    else:
                        task.state = TaskState.AVAILABLE
                case TaskState.UNSUCCESSFUL:
                    task.state = TaskState.AVAILABLE
                    # eventually add a lose task
                case TaskState.QUEUED:
                    print(f"Why is this task still queued? {task.name}")
                case TaskState.ONGOING:
                    # Do not change the state of ongoing tasks.
                    pass
            

            