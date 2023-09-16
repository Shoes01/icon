class Icon:
    def __init__(self, name: str, symbol: str, category: str):
        self.name = name
        self.symbol = symbol
        self.catgeory = category


def icon_factory(icon: str) -> Icon:
    match icon:
        #
        # XCOM
        #
        case "attack", "A":
            return Icon(
                name="Attack",
                symbol="A",
                category="xcom"
            )
        case "defend", "D":
            return Icon(
                name="Defend",
                symbol="D",
                category="xcom"
            )
        #
        # SIGINT
        #
        case "analysis":
            return Icon(
                name="Analysis",
                symbol="A",
                category="sigint"
            )
        case "observation":
            return Icon(
                name="Observation",
                symbol="O",
                category="sigint"
            )
        case "collection":
            return Icon(
                name="Collection",
                symbol="C",
                category="sigint"
            )
        #
        # SATCOM
        #
        case "communication":
            return Icon(
                name="Communication",
                symbol="C",
                category="satcom"
            )
        case "jamming":
            return Icon(
                name="Jamming",
                symbol="J",
                category="satcom"
            )
        case "deception":
            return Icon(
                name="Deception",
                symbol="D",
                category="satcom"
            )
        case "disruption":
            return Icon(
                name="Disruption",
                symbol="D",
                category="satcom"
            )
        case "denial":
            return Icon(
                name="Denial",
                symbol="D",
                category="satcom"
            )
