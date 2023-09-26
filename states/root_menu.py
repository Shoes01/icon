from base_state import BaseState
from states.main_screen import MainScreen
from print_color import print_VIP_text, print_regular_text


menu_title =\
"""
  _____ _____ ____  _   _          __    _____  ______      ________ _____  _   _ __  __ ______ _   _ _______ 
 |_   _/ ____/ __ \| \ | |        / _|  / ____|/ __ \ \    / /  ____|  __ \| \ | |  \/  |  ____| \ | |__   __|
   | || |   | |  | |  \| |   ___ | |_  | |  __| |  | \ \  / /| |__  | |__) |  \| | \  / | |__  |  \| |  | |   
   | || |   | |  | | . ` |  / _ \|  _| | | |_ | |  | |\ \/ / |  __| |  _  /| . ` | |\/| |  __| | . ` |  | |   
  _| || |___| |__| | |\  | | (_) | |   | |__| | |__| | \  /  | |____| | \ \| |\  | |  | | |____| |\  |  | |   
 |_____\_____\____/|_| \_|  \___/|_|    \_____|\____/   \/   |______|_|  \_\_| \_|_|  |_|______|_| \_|  |_|   
"""

class RootMenu(BaseState):
    def __init__(self):
        super().__init__(menu_title=menu_title, menu_options=["New Game", "Quit"], name="RootMenu")
    

    def render(self) -> None:
        print_VIP_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option}\n"
        print_regular_text(text)


    def handle_input(self, user_input: int):
        match user_input:
            case "1":
                return {"new_game": True}
            case "2":
                return {"quit", True}