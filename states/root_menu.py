from base_state import BaseState
from states.main_screen import MainScreen


class RootMenu(BaseState):
    def __init__(self):
        super().__init__(menu_title="ICON OF GOVERNMENT", menu_options=["New Game", "Quit"])
    

    def handle_input(self, user_input: int):
        match user_input:
            case 1:
                return {"new_game": True}
            case 2:
                return {"quit", True}