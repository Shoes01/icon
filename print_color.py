from colorama import Fore, Style, Back, init

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