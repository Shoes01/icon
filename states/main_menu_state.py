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
            print(
"""

  _   _ ________          __   _____          __  __ ______ 
 | \ | |  ____\ \        / /  / ____|   /\   |  \/  |  ____|
 |  \| | |__   \ \  /\  / /  | |  __   /  \  | \  / | |__   
 | . ` |  __|   \ \/  \/ /   | | |_ | / /\ \ | |\/| |  __|  
 | |\  | |____   \  /\  /    | |__| |/ ____ \| |  | | |____ 
 |_| \_|______|   \/  \/      \_____/_/    \_\_|  |_|______|
                                                            
                                                            
"""
            )
            self.mediator.change_state(self.mediator.play_state)
        elif user_input == "2":
            self.mediator.change_state(self.mediator.settings_state)

    def update(self):
        pass