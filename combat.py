from colorama import init, Fore, Style
import random
from typing import Dict, Any, List
import os

from task import Task, TaskState
from team import Team, TeamState
from print_color import print_regular_text, print_text_input, print_good_text, print_bad_text, print_important_text, print_good_combat_text, print_bad_combat_text


def do_combat(team: Team, task: Task) -> Dict[str, Any]:
    team_icon_names: List[str] = [icon.name for icon in team.icons]
    task_icon_pattern: List[str] = [random.choice(task.icons) for _ in range(20)]

    #print_regular_text(f"{team.name.title()} has the following icons: {team_icon_names}.")
    #print_regular_text(f"{task.name.title()} has the following pattern: {[icon.name for icon in task.icons]}.")

    # Prepare the terminal for combat!
    os.system('cls' if os.name == 'nt' else 'clear')
    terminal_size = os.get_terminal_size()
    num_lines = max(12, terminal_size.lines - 2)
    print(f"\033[{num_lines}A", end="")

    print_important_text(f"{task.name.upper()}.", slow_print=True)
    print_regular_text("\n" + task.description + "\n", slow_print=True)
    
    wins = 0
    losses = 0
    success = False
    for icon in task_icon_pattern:
        if icon.name in team_icon_names:
            print_important_text("[+]", end="", slow_print=True)
            print_good_combat_text(f" : {task.barks[wins]}", slow_print=True)
            wins += 1
        else:
            print_bad_text("[-]", end="", slow_print=True)
            print_bad_combat_text(f" : {task.fail_barks[wins]}", slow_print=True)
            losses += 1
        
        if wins >= task.wincon:
            print_good_text(f"\n{task.barks[-1]}\n", slow_print=True)
            success = True
            break
        elif losses >= task.losecon:
            print_bad_text(f"\n{task.fail_barks[-1]}\n", slow_print=True)
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

    return {"combat": (team, task)}


def do_combat_SIGINT_fromAI(team: Team, task: Task) -> Dict[str, Any]:
    # Define the task requirements
    # EXAMPLE:
    ### task_requirements = {
    ###     "Analysis": {"Analysize": 6, "Holographic Encryption": 2},
    ###     "Encryption": {"Holographic Encryption": 4, "Decryption": 3},
    ###     "Decryption": {"Decryption": 5, "Analysize": 2}
    ### }
    task_requirements = task.requirements 

    # Define the initial task status
    task_status = {task: {icon: 0 for icon in requirements} for task, requirements in task_requirements.items()}

    # Define the maximum number of incorrect matches allowed
    max_incorrect_matches = 4

    # Define the current number of incorrect matches
    incorrect_matches = 0

    # Loop until the combat is won or lost
    while True:
        # TODO: Implement code to display the current task status and prompt the user for input

        # TODO: Implement code to update the task status based on the user's input

        # Check if the combat has been won
        if all(icon_count >= required_count for requirements in task_requirements.values() for icon, required_count in requirements.items() for task, icon_count in task_status.items() if task in task_requirements and icon in requirements):
            print("Combat won!")
            break

        # Check if the combat has been lost
        if incorrect_matches >= max_incorrect_matches:
            print("Combat lost!")
            break