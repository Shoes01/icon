from base_state import BaseState

title = "Where do you want to go?"
options = ["SIGINT", "SATCOM", "XCOM", "End Turn"]

class MainScreen(BaseState):
    def __init__(self):
        super().__init__(menu_title=title, menu_options=options)
    
    def handle_input(self, user_input: int):
        match user_input:
            case 1:
                return {"sigint": True}
            case 2:
                return {"satcom": True}
            case 3:
                return {"xcom": True}
            case 4:
                return {"end_turn": True}