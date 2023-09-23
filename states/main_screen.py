from typing import Dict, List

from base_state import BaseState
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_important_text, print_good_text


title = "Welcome, commander."
options = ["SIGINT", "SATCOM", "XCOM", "Task Queue"]


class MainScreen(BaseState):
    def __init__(self, alerts: Dict[str, int], tasks: List[Task], teams: List[Team]):
        super().__init__(menu_title=title, menu_options=options, name="MainScreen")
        self.alerts = alerts
        self.tasks = tasks
        self.teams = teams
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
        text = ""
        for i, option in enumerate(self.menu_options):
            text += f"{i+1}. {option:<8}"
            if option.lower() in ["sigint", "satcom", "xcom"]:
                # Add the number of tasks for each option
                tasks_available = 0
                tasks_queued = 0
                for task in self.tasks:
                    if task.category == option.lower() and option.lower() != "task queue": # TODO: This is lazy. It's matching the name of the option to the type of task.
                        match task.state:
                            case TaskState.AVAILABLE:
                                tasks_available += 1
                            case TaskState.QUEUED:
                                tasks_queued += 1
                s1 = "" if tasks_available == 1 else "s"
                s2 = "" if tasks_queued == 1 else "s"
                text += f"\n  > {tasks_available} task{s1} available, {tasks_queued} task{s2} queued."
                teams_available = 0
                teams_on_cooldown = 0
                for team in self.teams:
                    if team.category == option.lower(): # TODO: This is lazy, too.
                        match team.state:
                            case TeamState.AVAILABLE:
                                teams_available += 1
                            case TeamState.COOLDOWN:
                                teams_on_cooldown += 1
                s1 = "" if teams_available == 1 else "s"
                s2 = "" if teams_on_cooldown == 1 else "s"
                text += f"\n  > {teams_available} team{s1} available, {teams_on_cooldown} team{s2} on cooldown.\n"
            elif option.lower() == "task queue":
                tasks_in_queue = 0
                for task in self.tasks:
                    if task.state == TaskState.QUEUED:
                        tasks_in_queue += 1
                s = "" if tasks_in_queue == 1 else "s"
                text += f"\n  > {tasks_in_queue} task{s} in queue.\n"
        text += "\n0. End Turn"
        print_regular_text(text)

        # Print teams as well.


    def handle_input(self, user_input: int):
        match user_input:
            case 1:
                return {"sigint": True}
            case 2:
                return {"satcom": True}
            case 3:
                return {"xcom": True}
            case 4:
                return {"task_queue": True}
            case 0:
                self.alters_are_read = False
                return {"end_turn": True}