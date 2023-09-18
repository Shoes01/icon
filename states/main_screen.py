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
        
        # Print alerts, if any.
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
        
        # Print departments and their tasks.
        # TODO: be more clear about tasks that are which state.
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option.upper():<8}"
            # Add the number of tasks for each option
            tasks_available = 0
            tasks_in_progress = 0
            for task in self.tasks:
                if task.category == option:
                    match task.state:
                        case TaskState.AVAILABLE:
                            tasks_available += 1
                        case TaskState.IN_PROGRESS:
                            tasks_in_progress += 1
            s1 = "" if tasks_available == 1 else "s"
            s2 = "" if tasks_in_progress == 1 else "s"
            text += f"\n  > {tasks_available} task{s1} available, {tasks_in_progress} task{s2} in progress.\n"
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