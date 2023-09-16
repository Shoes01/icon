from colorama import init, Fore, Style
import random
from typing import Dict, Any, List

from task import Task
from team import Team
from print_color import print_regular_text, print_text_input


def do_combat(team: Team, task: Task) -> Dict[str, Any]:
    team_icon_names: List[str] = [icon.name for icon in team.icons]
    task_icon_pattern: List[str] = [random.choice(task.icons) for _ in range(10)]

    print_regular_text(f"{team.name.title()} has the following icons: {team_icon_names}.")
    print_regular_text(f"{task.name.title()} has the following pattern: {[icon.name for icon in task.icons]}.")
    print_regular_text("\n" + task.description + "\n")
    wins = 0
    for icon in task_icon_pattern:
        if icon.name in team_icon_names:
            wins += 1
            #print(f"[+] : {random.choice(icon.bark_win)}")
            print(f"{Fore.GREEN}[+]{Style.RESET_ALL} : {random.choice(icon.bark_win)}")
        else:
            print(f"{Fore.RED}{Style.BRIGHT}[-]{Style.RESET_ALL} : {Fore.BLACK}{random.choice(icon.bark_lose)}{Style.RESET_ALL}")
    print_regular_text(f"\nWin percentage was {int(wins / len(task_icon_pattern) * 100)}%.")
    
    print_text_input("\nPress any key to conclude combat.\n")
    input()

    return {"combat": True}
