class SettingsState:
    def __init__(self, mediator):
        self.mediator = mediator

    def render(self):
        print(
"""
SETTINGS STATE

There are no settings. Press "q" to return to main menu.
"""
        )

    def handle_input(self, user_input):
        pass

    def update(self):
        pass