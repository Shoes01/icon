class Team:
    def __init__(self, name, category):
        self.name = name
        self.category = category

def team_factory(team: str) -> Team:
    match team:
        case "sigint":
            return Team(
                name="SIGINT Team", 
                category="sigint")
        case "satcom":
            return Team(
                name="SATCOM Team", 
                category="satcom")
        case "xcom":
            return Team(
                name="XCOM Team", 
                category="xcom")