import random
from typing import Dict, Any, List

from task import Task
from team import Team


def do_combat(team: Team, task: Task) -> Dict[str, Any]:
    team_icon_names: List[str] = [icon.name for icon in team.icons]
    task_icon_pattern: List[str] = [random.choice(task.icons) for _ in range(10)]

    print(f"{team.name.title()} has the following icons: {team_icon_names}.")
    print(f"{task.name.title()} has the following pattern: {[icon.name for icon in task.icons]}.")
    print("\nPrepare for combat!\n")
    wins = 0
    for icon in task_icon_pattern:
        if icon.name in team_icon_names:
            wins += 1
            print(f"TEAM SUCCESFUL! Task used {icon.name} ({icon.symbol}).")
        else:
            print(f"TEAM FAILURE.   Task used {icon.name} ({icon.symbol}).")
    print(f"Win percentage was {int(wins / len(task_icon_pattern) * 100)}%.\n")
    input("\nPress any key to conclude combat.\n")

    return {"combat": True}
