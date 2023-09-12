import random
from typing import List
from unit import Unit
from icons import Icon


def do_combat(attacker: Unit, defender: Unit):
    attacker_icons_names = [icon.name for icon in attacker.icons]
    defender_pattern: List[str] = [random.choice(defender.icons) for _ in range(10)]

    print(f"{attacker.name.title()} has the following icons: {attacker_icons_names}.")
    print(f"{defender.name.title()} has the following pattern: {[icon.name for icon in defender.icons]}.")
    print("\nPrepare for combat!\n")
    wins = 0
    for icon in defender_pattern:
        if icon.name in attacker_icons_names:
            wins += 1
            print(f"ATTACKER SUCCESFUL! Defender used {icon.name} ({icon.symbol}).")
        else:
            print(f"ATTACKER FAILURE.   Defender used {icon.name} ({icon.symbol}).")
    print(f"Win percentage was {int(wins / len(defender_pattern) * 100)}%.\n")

    input("\nPress any key to conclude combat.\n")
    
