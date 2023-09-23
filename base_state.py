from typing import List, Dict, Any

from print_color import print_text_error, print_regular_text, print_important_text


class BaseState:
    def __init__(self, menu_title: str, menu_options: List[str], name: str = "BaseState"):
        self.menu_title = menu_title
        self.menu_options = menu_options
        self.name = name


    def render(self) -> None:
        print_important_text(self.menu_title)
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option}\n"
        print_regular_text(text)
    

    def handle_input(self, user_input: int) -> Dict[str, Any]:
        print_text_error("DEBUG: BaseState.handle_input() called")
        return {"nothing": False}
    
    
    def sanitize_input(self, user_input: str) -> int:
        #I don't think I like this anymore.
        try:
            user_input = int(user_input)
            return user_input
        except ValueError:
            print_text_error("Invalid input. Please enter a number.")
            return -1