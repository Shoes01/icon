from typing import Dict, Any

from task import Task
from team import Team


def do_combat(team: Team, task: Task) -> Dict[str, Any]:
    return {"combat": f"{team.name} is doing {task.name}, and was victorious!"}