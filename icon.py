from typing import List


class Icon:
    def __init__(self, name: str, symbol: str, category: str, color: str, bark_win: List[str] = None, bark_lose: List[str] = None):
        self.name = name
        self.symbol = symbol
        self.catgeory = category
        self.bark_win = bark_win
        self.bark_lose = bark_lose
        self.color = "white"
        if color in ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]:
            self.color = color
        else:
            print(f"Invalid color {color} for icon {name}. Defaulting to white.")


def icon_factory(icon: str) -> Icon:
    match icon:
        #
        # XCOM
        #
        case "attack", "A":
            return Icon(
                name="Attack",
                symbol="A",
                category="xcom",
                color="green",
            )
        case "defend", "D":
            return Icon(
                name="Defend",
                symbol="D",
                category="xcom",
                color="green",
            )
        #
        # SIGINT
        #
        case "analysis":
            return Icon(
                name="Analysis",
                symbol="A",
                category="sigint",
                color="magenta",
                bark_win = ["Signal fragment deciphered", "Data chunk decoded.", "Signal encryption layer breached", "Signal partially decrypted.", "Frequency pattern identified."],
                bark_lose = ["Signal fragment lost", "Data chunk corrupted."]
            )
        case "observation":
            return Icon(
                name="Observation",
                symbol="O",
                category="sigint",
                color="magenta",
                bark_win=["Something was seen :)"],
                bark_lose=["SIGINT team status: no signals detected. Continuing surveillance.","Signal silence persists: alien communication remains elusive.","Transmission absence: patience required. Standby for activity."]
            )
        case "collection":
            return Icon(
                name="Collection",
                symbol="C",
                category="sigint",
                color="magenta",
            )
        #
        # SATCOM
        #
        case "communication":
            return Icon(
                name="Communication",
                symbol="C",
                category="satcom",
                color="yellow",
            )
        case "jamming":
            return Icon(
                name="Jamming",
                symbol="J",
                category="satcom",
                color="yellow",
            )
        case "deception":
            return Icon(
                name="Deception",
                symbol="D",
                category="satcom",
                color="yellow",
            )
        case "disruption":
            return Icon(
                name="Disruption",
                symbol="D",
                category="satcom",
                color="yellow",
            )
        case "denial":
            return Icon(
                name="Denial",
                symbol="D",
                category="satcom",
                color="yellow",
            )
