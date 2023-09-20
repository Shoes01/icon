from typing import List
from enum import Enum

from icon import Icon, icon_factory


class TaskState(Enum):
    AVAILABLE = 1
    IN_PROGRESS = 2
    SUCCESSFUL = 3
    UNSUCCESSFUL = 4
    CHOSEN = 5
    QUEUED = 6


class Task:
    task_counter = 0

    def __init__(self, name: str, description: str, category: str, icons: List[Icon], wincon: int, losecon: int, barks: List[str] = [], fail_barks: List[str] = [], win_tasks: List[str] = [], lose_tasks: List[str] = []):
        self.name = name
        self.description = description # not really a description, more like the opening bark.
        self.category = category
        self.icons = icons
        self.wincon = wincon
        self.losecon = losecon
        self.barks = barks
        self.fail_barks = fail_barks
        self.win_tasks = win_tasks

        self.state = TaskState.AVAILABLE
        self.id = Task.task_counter
        Task.task_counter += 1


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
                description="Task Scanning frequency bands for unusual signal patterns...", 
                category="sigint",
                icons=[icon_factory("analysis"), icon_factory("analysis"), icon_factory("observation")],
                wincon=6,
                win_tasks=["sigint_2", "satcom_1"],
                losecon=4,
                barks=[
                    "Preliminary sweeps complete. Slight irregularities in signal background observed: begin signal optimization.",     #0
                    "Optimization ongoing. Possible faint anomalies in signal patterns noted: refining parameters",                     #1
                    "Optimization complete: Alien signal detected, still weak and intermittent. Begin signal analysis via FTT.",        #2
                    "Fast-Fourier Transform underway: frequency spectrum dissected; unique spectral patterns identified. Implementing PCA.", #3
                    "Signal analysis update: PCA identified key components. Proritizing data for further analysis.",     #4
                    "Analysis complete: reliable reception of alien communications achieved.",                                          #5
                    "Extraterrestrial signal detection and analysis successful.",                                                       # The victory bark.
                ],
                fail_barks=[
                    "No unusual patterns detected... recalibrating...",                                                                 #0
                    "Unusual signal interference detected, disrupting initial scans.",                                                  #1
                    "Irregularities persist, obscuring further observations.",                                                          #2
                    "Analysis setback: FFT algorithm struggles to reveal spectral patterns in the elusive alien transmission.",         #3
                    "PCA challenge: Critical components in the alien transmission elude identification, complicating prioritization.",  #4
                    "Parameters adjustment faltering: Alien signal weakens further, intermittent transmission disrupts analysis.",      #5 -- I don't think this one will ever be seen?
                    "Reliability compromised: alien signal is lost.",                                                                   # The failure bark.
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
        case "satcom_1":
            return Task(
                name="Signal Source Tracking",
                description="Task initiated: Position satellite arrays to pinpoint source location...",
                category="satcom",
                icons=[icon_factory("observation"), icon_factory("communication"), icon_factory("jamming")],
                wincon=6,
                losecon=4,
                barks=[
                    "Origin assessment complete: Signal source localized to specified coordinates; now leveraging differential GPS data for precise satellite array configuration.",
                    "Satellite array configured for optimal coverage over signal source region; implementing orbital adjustment with real-time data from differential GPS systems.",
                    "Orbital adjustment successful, ensuring continuous coverage; initiating frequency monitoring with adaptive beamforming techniques for enhanced accuracy.",
                    "Frequency monitoring activated with real-time data stream; commencing data correlation, utilizing advanced machine learning algorithms for pattern recognition.",
                    "Data correlation successfully accomplished, source triangulated with precision; advancing to establish real-time tracking with Kalman filtering for accurate predictions.",
                    "Real-time tracking operational, monitoring signal source movements; proceeding to execute data relay, integrating geospatial data for context-aware relay decisions.",
                    "Data relay successfully executed, tracking data and source information transmitted; progressing to maintain continuous monitoring with data fusion from multiple sensors.",
                    "Continuous monitoring in progress, signal source tracked and updated; maintaining situational awareness through the integration of geospatial databases and real-time signal analysis.",
                ],
                fail_barks=[
                    "Setback encountered: Differential GPS data fluctuations affecting precise satellite array configuration; recalibrating for accuracy.",
                    "Adjustment challenges: Real-time differential GPS data discrepancies impact orbital configuration; readjusting for consistent coverage.",
                    "Beamforming hiccups: Adaptive beamforming limitations affecting frequency monitoring accuracy; optimizing for reliable data.",
                    "Data correlation complexity: Machine learning algorithm challenges affecting pattern recognition; refining for precise data correlation.",
                    "Kalman filtering difficulties: Precision in real-time tracking hampered by parameter adjustments; recalibrating for improved accuracy.",
                    "Integration issues: Geospatial data inconsistencies impacting context-aware relay decisions during data relay; revising integration protocols.",
                    "Fusion challenges: Data fusion complexities affecting real-time sensor collaboration; optimizing for seamless continuous monitoring.",
                    "Signal source tracking failed: geospatial database reliability unusable.",
                ],
            )