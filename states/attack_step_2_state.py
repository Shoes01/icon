from constants import NUMBER_OPTIONS
from typing import List
from unit import Unit

class AttackState_2:
    def __init__(self, mediator):
        self.mediator = mediator
        self.unit_list: List[Unit] = []
        self.menu_list: str = ""
        self.chosen_task = self.mediator.attack_state_1.chosen_task

    def render(self):
        print(
f"""
ATTACK STATE 2/2

Which task are you undertaking?

{self.unit_list}

q. Nevermind.
"""
        )

    def handle_input(self, user_input):
        if user_input.isdigit() and int(user_input) < len(self.unit_list):
            print(f"You are performing task {self.task_list[int(user_input).name.title()]}. Now choose a unit.")        

    def update(self):
        # Prepare the list of options from the menu.
        self.unit_list = []
        for unit in self.mediator.game.player.units:
            if unit.type == "attacker":
                self.unit_list.append(unit)
        
        iterator = 0
        self.menu_list = ""
        for unit in self.unit_list:
            self.menu_list += str(NUMBER_OPTIONS[iterator]) + ". " + unit.name.title() + "\n"
            iterator += 1
            
            if iterator == len(NUMBER_OPTIONS): break


