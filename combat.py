import random
from typing import List


def generate_defender_pattern(defender) -> List:
    defender_icons: List = defender.icons
    return [random.choice(defender_icons) for _ in range(10)]

def do_combat(attacker, defender):
    attacker_icons: List = attacker.icons

    defender_pattern: List = generate_defender_pattern(defender)

    for icon in defender_pattern:
        if icon in attacker_icons:
            print(f"Defender used {icon}. It was not very effective.")
        else:
            print(f"Defender used {icon}. It was super effective!")