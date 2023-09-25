import random
from typing import Dict, Any, List
import os
import time
import random

from debug_options import DEBUG_ALWAYS_PRINT_FAST, DEBUG_ALWAYS_SHOW_VERBOSE_COMBAT
from icon import Icon
from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_text_input, print_good_text, print_bad_text, print_important_text, print_good_combat_text, print_bad_combat_text


def do_combat(team: Team, task: Task) -> Dict[str, Any]:
    team_icons: Dict[Icon, int] = team.icons
    team_icon_names: Dict[str, int] = {icon.name: count for icon, count in team_icons.items()}

    task_icons: Dict[Icon, int] = task.icons
    task_icon_pattern: List[Icon] = [icon for icon, count in task_icons.items() for _ in range(count)]
    random.shuffle(task_icon_pattern)  

    #print_regular_text(f"{team.name.title()} has the following icons: {team_icon_names}.")
    #print_regular_text(f"{task.name.title()} has the following pattern: {[icon.name for icon in task.icons]}.")

    # Prepare the terminal for combat!
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal_size = os.get_terminal_size()
    num_lines = max(12, terminal_size.lines - 2)
    print(f"\033[{num_lines}A", end="")

    print_important_text(f"{task.name.upper()}", slow_print=True)
    print_regular_text("\n" + task.description + "\n", slow_print=True)
    
    wins = 0
    losses = 0
    success = False
    for icon in task_icon_pattern:
        if DEBUG_ALWAYS_SHOW_VERBOSE_COMBAT: print_bad_text(f"{team_icon_names=} :: using {icon.name=}")
        choice = random.randint(0, len(task.steps) - 1)
        print_good_combat_text(f"{task.steps[choice][wins][0][:-1]}", end="", slow_print=True) # Don't print the final period.
        # print a random number of periods between 1 and 4.
        if not DEBUG_ALWAYS_PRINT_FAST: 
            for _ in range(random.randint(2, 6)):
                time.sleep(0.2)
                print(".", end="")
            time.sleep(0.2)
            print(" ", end="")

        if icon.name in team_icon_names and team_icon_names[icon.name] > 0:
            print_important_text("[+]", end="", slow_print=False)
            print_good_combat_text(f" {task.steps[choice][wins][1]}", slow_print=True)
            team_icon_names[icon.name] -= 1
            wins += 1
        else:
            print_bad_text("[-]", end="", slow_print=False)
            print_bad_combat_text(f" {task.steps[choice][wins][2]}", slow_print=True)
            losses += 1
        
        if wins >= task.wincon:
            print_good_text(f"\n{task.bark_win}\n", slow_print=True)
            success = True
            break
        elif losses >= task.losecon:
            print_bad_text(f"\n{task.bark_fail}\n", slow_print=True)
            success = False
            break
    
    if success:
        task.state = TaskState.SUCCESSFUL
    else:
        task.state = TaskState.UNSUCCESSFUL
    
    team.state = TeamState.COOLDOWN
    team.cooldown = losses + 1

    print_text_input("\nPress any key to conclude combat.\n")
    input()

    return {"combat": True}