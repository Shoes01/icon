class Icon:
    def __init__(self, type="generic"):
        match type.lower():
            case "attack":
                self.name = "Attack Icon"
                self.symbol = "A"
            case "defend":
                self.name = "Defend Icon"
                self.symbol = "D"
            case "generic":
                self.name = "Generic Icon"
                self.symbol = "G"