from colorama import Fore, Style, Back, init
from typing import List

from task import Task, TaskState
from team import Team, TeamState


init()


def print_color(text: str, fore: str="normal", back: str="normal", style: str="normal", end: str="\n"):
    output: str = ""
    
    match fore:
        case "normal":
            output += f"{Fore.WHITE}"
        case "green":
            output += f"{Fore.GREEN}"
        case "red":
            output += f"{Fore.RED}"
        case "black":
            output += f"{Fore.BLACK}"
    
    match back:
        case "normal":
            output += f"{Back.BLACK}"
        case "green":
            output += f"{Back.GREEN}"
    
    match style:
        case "normal":
            output += f"{Style.NORMAL}"
        case "bright":
            output += f"{Style.BRIGHT}"
        case "dim":
            output += f"{Style.DIM}"
    
    output += f"{text}{end}{Style.RESET_ALL}"
    print(output, end="")


def print_text_input(text: str, end: str=""):
    print_color(text, fore="black", back="green", style="bright", end=end)


def print_text_error(text: str, end: str="\n"):
    print_color(text, fore="red", end=end)


def print_important_text(text: str, end: str="\n"):
    print_color(text, fore="green", style="bright", end=end)


def print_regular_text(text: str, end: str="\n"):
    print_color(text, fore="green", end=end)


def print_VIP_text(text: str, end: str="\n"):
    print_color(text, fore="black", back="green", style="bright", end=end)


def print_good_text(text: str, end: str="\n"):
    print_color(text, fore="cyan", style="bright", end=end)


def print_bad_text(text: str, end: str="\n"):
    print_color(text, fore="red", style="bright", end=end)


def print_two_columns(col_teams: List[Task], col_tasks: List[Team], col_width: int=60):
    header = "TEAMS" + " "*(col_width-5) + "TASKS"
    print_important_text(header)

    menu_length = max(len(col_tasks), len(col_teams))
    for i in range(menu_length):
        team = ""
        task = ""
        naked_team_length = 0

        if len(col_teams) == 0 and i == 0:
            team = "There are no teams."
            naked_team_length = len(team)
            team = Fore.GREEN + team + Style.RESET_ALL
        if len(col_tasks) == 0 and i == 0:
            task = Fore.GREEN + "There are no tasks." + Style.RESET_ALL

        if len(col_tasks) > i:
            task = f"{i+1}. {col_tasks[i].name}"

            match col_tasks[i].state:
                case TaskState.CHOSEN:
                    task = f"{Fore.BLACK}{Back.GREEN}{Style.BRIGHT}{task}{Style.RESET_ALL}"
                case TaskState.IN_PROGRESS:
                    task = f"{Fore.YELLOW}{task}{Style.RESET_ALL}"
                case TaskState.AVAILABLE:
                    task = f"{Fore.GREEN}{task}{Style.RESET_ALL}"
        
        if len(col_teams) > i:
            team = f"{i+1}. {col_teams[i].name}"
            if col_teams[i].cooldown > 0:
                team += f" ({col_teams[i].cooldown} turns)"
            naked_team_length = len(team)

            match col_teams[i].state:
                case TeamState.AVAILABLE:
                    team = f"{Fore.GREEN}{team}{Style.RESET_ALL}"
                case TeamState.WORKING:
                    team = f"{Fore.YELLOW}{team}{Style.RESET_ALL}"
                case TeamState.COOLDOWN:
                    team = f"{Fore.RED}{team}{Style.RESET_ALL}"
                case TeamState.CHOSEN:
                    team = f"{Fore.BLACK}{Back.GREEN}{Style.BRIGHT}{team}{Style.RESET_ALL}"
        
        needed_padding = col_width - naked_team_length
        print(team + " "*needed_padding + task)
    
    print()
