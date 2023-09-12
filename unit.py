from typing import List
from icons import Icon

class Unit:
    def __init__(self, type="generic"):
        match type.lower():
            case "soldier":
                self.name = "Soldier"
                self.icons = [Icon("attack")]
                self.type = "attacker"
            case "generic":
                self.name: str = "Generic Unit"
                self.icons: List[Icon] = [Icon("attack"), Icon("defend"), Icon()]
                self.type = "generic"