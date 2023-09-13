class Icon:
    def __init__(self, type="generic"):
        match type.lower():
            case "attack", "A":
                self.name = "Attack Icon"
                self.symbol = "A"
            case "defend", "D":
                self.name = "Defend Icon"
                self.symbol = "D"
            case "generic", "G":
                self.name = "Generic Icon"
                self.symbol = "G"