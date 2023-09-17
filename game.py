from typing import List, Dict, Any
import os

from base_state import BaseState
from states.root_menu import RootMenu
from states.main_screen import MainScreen
from states.sigint_screen import SigintScreen
from task import Task, task_factory
from team import Team, team_factory
from combat import do_combat
from print_color import print_regular_text, print_text_input, print_important_text

class Game:
    def __init__(self):
        self.running = True
        self.state_stack: List[BaseState] = [RootMenu(),]
        self.turn_count = 0
        self.tasks: Dict[str, List[Task]] = {
            "sigint": [],
            "satcom": [],
            "xcom": [],
        }
        self.teams: Dict[str, List[Team]] = {
            "sigint": [],
            "satcom": [],
            "xcom": [],
        }

        self.add_team(team_factory("sigint"))
        self.alerts: Dict[str, int] = {"sigint": 0, "satcom": 0, "xcom": 0}


    def push_state(self, state: BaseState):
        self.state_stack.append(state)
    

    def pop_state(self):
        if len(self.state_stack) == 1:
            self.quit()
        else:
            self.state_stack.pop()


    def run(self):
        while self.running:
            #os.system('cls' if os.name == 'nt' else 'clear')
            self.state_stack[-1].render()
            
            if len(self.state_stack) > 1:
                print_regular_text("b. Back\n")

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
                self.pop_state()
                user_input = ""
        return user_input


    def end_turn(self):
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
                    self.state_stack.append(MainScreen(self.alerts, self.tasks))
                case "quit":
                    self.quit()
                case "end_turn":
                    self.end_turn()
                case "sigint":
                    self.state_stack.append(SigintScreen(tasks=self.tasks["sigint"], teams=self.teams["sigint"]))
                case "task":
                    task: Task = value[0]
                    team: Team = value[1]
                    result = do_combat(team, task)
                    self.update(result)
                case "combat":
                    current_task: Task = value
                    for task in self.tasks[current_task.category]:
                        if task.name == current_task.name:
                            task.is_complete = current_task.is_complete
                    self.pop_state()


    def add_team(self, team: Team):
        self.teams[team.category].append(team)
    

    def add_task(self, task: Task):
        self.tasks[task.category].append(task)
        self.alerts[task.category] += 1


    def remove_task(self, task: Task):
        self.tasks[task.category].remove(task)


    def update_tasks(self, task: Task = None):
        if self.turn_count == 1:
            self.add_task(task_factory("sigint_1"))
        for tasks in self.tasks.values():
            for task in tasks:
                if task.name == "SIGINT Task" and task.is_complete:
                    self.add_task(task_factory("sigint_2"))
                if task.is_complete:
                    self.remove_task(task)

            