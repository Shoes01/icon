from constants import NUMBER_OPTIONS
from typing import List
import combat
from unit import Unit

class AttackState:
    def __init__(self, mediator):
        self.mediator = mediator
        self.unit_list: List = []
        self.menu_list: str = ""

    def render(self):
        print(
f"""
ATTACK STATE

Who will you attack with?

{self.menu_list}
q. Nevermind.
"""
        )

    def handle_input(self, user_input):
        if user_input.isdigit() and int(user_input) < len(self.unit_list):
            print(f"You are attacking with {self.unit_list[int(user_input)].name.title()}")
            generic_defender = Unit("generic")
            combat.do_combat(self.unit_list[int(user_input)], generic_defender)
            
    

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


