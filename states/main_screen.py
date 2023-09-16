from base_state import BaseState
from print_color import print_regular_text, print_important_text


title = "Where do you want to go?"
options = ["SIGINT", "SATCOM", "XCOM"]


class MainScreen(BaseState):
    def __init__(self):
        super().__init__(menu_title=title, menu_options=options)
    

    def render(self):
        print_important_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option}\n"
        text += "0. End Turn"
        print_regular_text(text)


    def handle_input(self, user_input: int):
        match user_input:
            case 1:
                return {"sigint": True}
            case 2:
                return {"satcom": True}
            case 3:
                return {"xcom": True}
            case 0:
                return {"end_turn": True}