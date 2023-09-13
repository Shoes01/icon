from mediator import Mediator
from player import Player

from typing import List
from tasks import Task, task_factory


class Game:
    def __init__(self):
        self.mediator = Mediator(self)
        self.running = True
        self.state_stack = [self.mediator.main_menu_state,]
        self.current_state = self.state_stack[-1]
        self.player = Player()
        self.turn_count = 0
        self.task_stack: List[Task] = []

    def change_state(self, new_state):
        self.state_stack.append(new_state)
        self.current_state = self.state_stack[-1]

    def previous_state(self):
        self.state_stack.pop()
        if len(self.state_stack) == 0:
            self.running = False
        else:
            self.current_state = self.state_stack[-1]

    def run(self):
        while self.running:
            self.current_state.render()
            user_input = input(f"[TURN:{self.turn_count}]> ").lower()
            self.handle_input(user_input)
            self.current_state.handle_input(user_input)
            self.update()
            self.current_state.update()
    
    def handle_input(self, user_input):
        if user_input == "q":
            self.previous_state()
        elif user_input == "x":
            self.quit()
        user_input = "" # consume the user input so the states can't use it.


    def update(self):
        if self.turn_count == 1:
            self.task_stack.append(task_factory("test"))


    def quit(self):
        self.running = False
    
    def end_turn(self):
        self.turn_count += 1