from typing import Dict, List

from base_state import BaseState
from task import Task, TaskState
from print_color import print_regular_text, print_important_text, print_good_text


title = "Welcome, commander."
options = ["sigint", "satcom", "xcom"]


class MainScreen(BaseState):
    def __init__(self, alerts: Dict[str, int], tasks: List[Task]):
        super().__init__(menu_title=title, menu_options=options)
        self.alerts = alerts
        self.tasks = tasks
        self.alters_are_read = False


    def render(self):
        print_important_text(self.menu_title)
        
        if self.alters_are_read is False:
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
            self.alters_are_read = True
        
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.upper():<8}"
            # Add the number of tasks for each option
            task_count = 0
            for task in self.tasks:
                if task.category == option and task.state == TaskState.AVAILABLE:
                    task_count += 1
            text += f"[ {task_count:>1} task.  ]\n" if task_count == 1 else f"[ {task_count:>1} tasks. ]\n"
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
                self.alters_are_read = False
                return {"end_turn": True}