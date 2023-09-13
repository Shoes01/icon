from constants import NUMBER_OPTIONS
from typing import List
from tasks import Task

class AttackState_1:
    def __init__(self, mediator):
        self.mediator = mediator
        self.task_list: List[Task] = []
        self.menu_list: str = ""
        self.chosen_task: Task = None

    def render(self):
        print(
f"""
ATTACK STATE 1/2

Which task are you undertaking?

{self.menu_list}

q. Nevermind.
"""
        )

    def handle_input(self, user_input):
        if user_input.isdigit() and int(user_input) < len(self.task_list):
            print(f"You are performing task {self.task_list[int(user_input)].name.title()}. Now choose a unit.")        
            self.chosen_task = self.task_list[int(user_input)]
            self.mediator.change_state(self.mediator.attack_state_2)

    def update(self):
        # Prepare the list of options from the menu.
        self.task_list: List[Task] = []
        for task in self.mediator.game.task_stack:
            if task.category == "attack":
                self.task_list.append(task)
        
        iterator = 0
        self.menu_list = ""
        for task in self.task_list:
            self.menu_list += str(NUMBER_OPTIONS[iterator]) + ". " + task.name.title() + "\n"
            iterator += 1
            
            if iterator == len(NUMBER_OPTIONS): break


