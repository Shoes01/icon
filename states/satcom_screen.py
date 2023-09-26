from typing import List

from event import Event
from task import Task
from team import Team

from states.dept_screen import DeptScreen


title = "Welcome to SATELLITE COMMAND"
name = "SatcomScreen"


class SatcomScreen(DeptScreen):
    def __init__(self, tasks: List[Task], teams: List[Team], events: List[Event]):
        super().__init__(tasks=tasks, teams=teams, events=events, menu_title=title, state_name=name)