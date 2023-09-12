class MainMenuState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        print(
"""
MAIN MENU

1. Play
2. Settings
"""
        )

    def handle_input(self, user_input):
        if user_input == "1":
            self.mediator.change_state(self.mediator.play_state)
        elif user_input == "2":
            self.mediator.change_state(self.mediator.settings_state)

    def update(self):
        pass