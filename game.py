from typing import List, Dict, Any
import os

from base_state import BaseState
from states.root_menu import RootMenu
from states.main_screen import MainScreen
from states.sigint_screen import SigintScreen
from task import Task, task_factory, TaskState
from team import Team, team_factory
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
        while len(self.task_queue):
            task, team = self.task_queue.pop()
            do_combat(team, task)
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
                    sigint_tasks = self.get_tasks("sigint")
                    sigint_teams = self.get_teams("sigint")
                    self.state_stack.append(SigintScreen(tasks=sigint_tasks, teams=sigint_teams))
                case "task":
                    task: Task = value[0]
                    team: Team = value[1]
                    task.state = TaskState.IN_PROGRESS
                    self.task_queue.append((task, team))
                    # remove this task from the task list
                    self.pop_state()
                case "combat":
                    current_task: Task = value
                    for task in self.tasks:
                        if task.name == current_task.name:
                            # If I have two tasks with the same name, then some random one will be marked complete. Is this a problem?
                            task.state = current_task.state
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
        
        for task in self.tasks:
            if task.name == "SIGINT Task" and task.state == TaskState.SUCCESSFUL:
                self.add_task(task_factory("sigint_2"))
            
            match task.state:
                case TaskState.SUCCESSFUL:
                    self.remove_task(task)
                case TaskState.UNSUCCESSFUL:
                    task.state = TaskState.AVAILABLE
                case TaskState.IN_PROGRESS:
                    print(f"Why is this task still in progress? {task.name}")
            

            