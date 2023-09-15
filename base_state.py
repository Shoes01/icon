from typing import List, Dict, Any


class BaseState:
    def __init__(self, menu_title: str, menu_options: List[str]):
        self.menu_title = menu_title
        self.menu_options = menu_options


    def render(self):
        print(self.menu_title)
        for i, option in enumerate(self.menu_options):
            print(f"{i+1}. {option}")
    

    def handle_input(self, user_input: int) -> Dict[str, Any]:
        print("DEBUG: BaseState.handle_input() called")
        return {"nothing": False}
    
    
    def sanitize_input(self, user_input: str) -> int:
        try:
            user_input = int(user_input)
            if user_input < 1 or user_input > len(self.menu_options):
                print("Invalid choice. Please enter a number between 1 and ", len(self.menu_options))
                return -1
            else:
                return user_input
        except ValueError:
            print("Invalid input. Please enter a number.")
            return -1