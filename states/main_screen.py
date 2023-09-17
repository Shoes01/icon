from typing import Dict, List

from base_state import BaseState
from task import Task
from print_color import print_regular_text, print_important_text, print_good_text


title = "Welcome, commander."
options = ["sigint", "satcom", "xcom"]


class MainScreen(BaseState):
    def __init__(self, alerts: Dict[str, int], tasks: Dict[str, List[Task]]):
        super().__init__(menu_title=title, menu_options=options)
        self.alerts = alerts
        self.tasks = tasks


    def render(self):
        print_important_text(self.menu_title)
        
        new_alerts = 0
        for alert_number in self.alerts.values():
            if alert_number > 0:
                new_alerts += 1
        print_good_text("1 alert." if new_alerts == 1 else f"{new_alerts} alerts.")
        want_whitespace = True
        for alert in self.alerts.items():
            if alert[1] > 0: 
                print_good_text(f"  New {alert[0].upper()} tasks: {alert[1]}.")
                want_whitespace = False
        if want_whitespace: print()
        
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.upper():<8}"
            # Add the number of tasks for each option
            text += f"[ {len(self.tasks[option]):>1} task.  ]\n" if len(self.tasks[option]) == 1 else f"[ {len(self.tasks[option]):>1} tasks. ]\n"
        text += "\n0. End Turn"
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