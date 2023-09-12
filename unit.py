from typing import List
from icons import Icon

class Unit:
    def __init__(self, type):
        match type.lower():
            case "soldier":
                self.name = "Soldier"
                self.icons = [Icon("attack")]
                self.type = "attacker"
            case _:
                self.name: str = "Generic Unit"
                self.icons: List[Icon] = [Icon(), ]
                self.type = "generic"