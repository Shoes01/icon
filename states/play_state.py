class PlayState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        print(
"""
PLAY STATE

q. Quit
"""
        )

    def handle_input(self, user_input):
        if user_input == "q":
            self.mediator.previous_state()

    def update(self):
        pass