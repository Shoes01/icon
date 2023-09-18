from typing import List
from enum import Enum

from icon import Icon, icon_factory


class TeamState(Enum):
    AVAILABLE = 1
    WORKING = 2
    COOLDOWN = 3


class Team:
    def __init__(self, name: str, category: str, icons: List[Icon]):
        self.name = name
        self.category = category
        self.icons = icons

        self.state = TeamState.AVAILABLE
        self.cooldown = 0


def team_factory(team: str) -> Team:
    match team:
        case "sigint":
            return Team(
                name="SIGINT Team", 
                category="sigint",
                icons=[icon_factory("analysis")]
                )
        case "satcom":
            return Team(
                name="SATCOM Team", 
                category="satcom",
                icons=[icon_factory("communication"), icon_factory("jamming")]
                )
        case "xcom":
            return Team(
                name="XCOM Team", 
                category="xcom",
                icons=[icon_factory("attack"), icon_factory("defend")]
                )