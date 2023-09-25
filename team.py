from typing import Dict
from enum import Enum

from icon import Icon, icon_factory


class TeamState(Enum):
    AVAILABLE = 1
    WORKING = 2
    COOLDOWN = 3
    CHOSEN = 4


class Team:
    team_counter = 0
    
    def __init__(self, name: str, category: str, icons: Dict[Icon, int]):
        self.name = name
        self.category = category
        self.icons = icons

        self.state = TeamState.AVAILABLE
        self.cooldown = 0
        self.id = Team.team_counter
        Team.team_counter += 1


def team_factory(team: str) -> Team:
    match team:
        case "sigint":
            return Team(
                name="SIGINT Team", 
                category="sigint",
                icons={
                    icon_factory("communication"): 3,
                    icon_factory("analysis"): 3,
                    icon_factory("observation"): 4,
                },
            )
        case "satcom":
            return Team(
                name="SATCOM Team", 
                category="satcom",
                icons={
                    icon_factory("communication"): 6,
                    icon_factory("jamming"): 2,
                    icon_factory("denial"): 2,
                },
            )
        case "xcom":
            return Team(
                name="XCOM Team", 
                category="xcom",
                icons={
                    icon_factory("attack"): 6,
                    icon_factory("defend"): 4,
                },
            )