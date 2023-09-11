class BattleState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        print(
"""
BATTLE STATE
...yes this was copied from main menu state

1. Play
2. Settings
q. Quit
"""
        )

    def handle_input(self, user_input):
        if user_input == "1":
            self.mediator.change_state(self.mediator.play_state)
        elif user_input == "2":
            self.mediator.change_state(self.mediator.settings_state)
        elif user_input == "q":
            self.mediator.previous_state()

    def update(self):
        pass