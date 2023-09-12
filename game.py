from mediator import Mediator
from player import Player


class Game:
    def __init__(self):
        self.mediator = Mediator(self)
        self.running = True
        self.state_stack = [self.mediator.main_menu_state,]
        self.current_state = self.state_stack[-1]
        self.player = Player()

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
            user_input = input("> ").lower()
            self.handle_input(user_input)
            self.current_state.handle_input(user_input)
            self.current_state.update()
    
    def handle_input(self, user_input):
        if user_input == "q":
            self.previous_state()
        elif user_input == "x":
            self.quit()

    def quit(self):
        self.running = False