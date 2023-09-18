from typing import List
from enum import Enum

from icon import Icon, icon_factory


class TaskState(Enum):
    AVAILABLE = 1
    IN_PROGRESS = 2
    SUCCESSFUL = 3
    UNSUCCESSFUL = 4


class Task:
    def __init__(self, name: str, description: str, category: str, icons: List[Icon], wincon: int, losecon: int, barks: List[str], fail_barks: List[str] = None):
        self.name = name
        self.description = description
        self.category = category
        self.icons = icons
        self.wincon = wincon
        self.losecon = losecon
        self.barks = barks
        self.fail_barks = fail_barks

        self.state = TaskState.AVAILABLE


def task_factory(task: str) -> Task:
    match task:
        #
        # XCOM
        #
        case "xcom_1":
            return Task(
                name="XCOM Task",
                description="This is a EXTRATERRESTRIALS COMMAND task.",
                category="xcom",
                icons=[icon_factory("attack")],
                wincon=6,
                losecon=4,
            )
        #
        # SIGINT
        #
        case "sigint_1":
            return Task(
                name="Extraterrestrial Signal Detection and Analysis", 
                description="Task initiated: Scanning frequency bands for unusual signal patterns...", 
                category="sigint",
                icons=[icon_factory("analysis"), icon_factory("analysis"), icon_factory("observation")],
                wincon=6,
                losecon=4,
                barks=[
                "Preliminary sweeps complete: Slight irregularities in signal background observed.",
                "Signal optimization underway: Possible faint anomalies in signal patterns noted.",
                "Refining signal capture parameters: Alien signal detected, still weak and intermittent.",
                "Signal analysis underway: Employing FFT to dissect the frequency spectrum of the intercepted alien transmission, identifying unique spectral patterns.",
                "Signal analysis update: Implementing PCA to identify key components within the intercepted alien transmission, prioritizing data for further analysis.",
                "Reliable reception of alien communications now achieved.",
                "Extraterrestrial signal detection and analysis successful.", # The victory bark.
                ],
                fail_barks=[
                    "Task interrupted: Unusual signal interference detected, disrupting initial scans.",
                    "Sweeps thwarted: Irregularities persist, obscuring further observations.",
                    "Optimization hindered: Faint anomalies proving elusive, signal remains enigmatic.",
                    "Parameters adjustment faltering: Alien signal weakens further, intermittent transmission disrupts analysis.",
                    "Analysis halted: FFT algorithm struggles to reveal spectral patterns in the elusive alien transmission.",
                    "PCA challenge: Critical components in the alien transmission elude identification, complicating prioritization.",
                    "Reliability compromised: alien signal is lost.",
                ],
            )
        case "sigint_2":
            return Task(
                name="SIGINT Task 2",
                description="This is a SIGNALS INTELLIGENCE task (2).",
                category="sigint",
                icons=[icon_factory("observation")],
                wincon=6,
                losecon=4,
            )
        #
        # SATCOM
        #