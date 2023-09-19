from typing import List, Dict, Any
import os

from base_state import BaseState
from states.root_menu import RootMenu
from states.main_screen import MainScreen
from states.satcom_screen import SatcomScreen
from states.sigint_screen import SigintScreen
from task import Task, task_factory, TaskState
from team import Team, team_factory, TeamState
from combat import do_combat
from print_color import print_regular_text, print_text_input, print_important_text

class Game:
    def __init__(self):
        self.running = True
        self.state_stack: List[BaseState] = [RootMenu(),]
        self.turn_count = 0
        self.tasks: List[Task] = []
        self.teams: List[Team] = []

        self.add_team(team_factory("sigint"))
        self.add_team(team_factory("satcom"))
        self.alerts: Dict[str, int] = {"sigint": 0, "satcom": 0, "xcom": 0}
        self.task_queue: List[tuple[Task, Team]] = []


    def push_state(self, state: BaseState):
        self.state_stack.append(state)
    

    def pop_state(self):
        if len(self.state_stack) == 1:
            self.quit()
        else:
            self.state_stack.pop()


    def run(self):
        while self.running:
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
            if user_input != "":
                user_input = self.state_stack[-1].sanitize_input(user_input)
                if user_input != -1:
                    result = self.state_stack[-1].handle_input(user_input)
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
        while len(self.task_queue):
            task, team = self.task_queue.pop()
            do_combat(team, task)
        for team in self.teams:
            if team.cooldown > 0:
                team.cooldown -= 1
            if team.cooldown == 0:
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
                    tasks = self.get_tasks("satcom")
                    teams = self.get_teams("satcom")
                    self.state_stack.append(SatcomScreen(tasks=tasks, teams=teams))                    
                case "sigint":
                    tasks = self.get_tasks("sigint")
                    teams = self.get_teams("sigint")
                    self.state_stack.append(SigintScreen(tasks=tasks, teams=teams))
                case "task":
                    task: Task = value[0]
                    team: Team = value[1]
                    task.state = TaskState.IN_PROGRESS
                    team.state = TeamState.WORKING
                    self.task_queue.append((task, team))
                    self.pop_state()
                case "combat":
                    current_task: Task = value[0]
                    current_team: Team = value[1]
                    for task in self.tasks:
                        if task.name == current_task.name:
                            # If I have two tasks with the same name, then some random one will be marked complete. Is this a problem?
                            task.state = current_task.state
                            break
                    for team in self.teams:
                        if team.name == current_team.name:
                            # If I have two tasks with the same name, then some random one will be marked complete. Is this a problem?
                            team.state = current_team.state
                            team.cooldown = current_team.cooldown
                            break
    
    
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
        
        for task in self.tasks:
            if task.state == TaskState.SUCCESSFUL:
                self.add_task(task_factory("sigint_2"))
            
            match task.state:
                case TaskState.SUCCESSFUL:
                    self.remove_task(task)
                case TaskState.UNSUCCESSFUL:
                    task.state = TaskState.AVAILABLE
                case TaskState.IN_PROGRESS:
                    print(f"Why is this task still in progress? {task.name}")
            

            