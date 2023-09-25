from typing import List, Tuple, Dict
from enum import Enum

from icon import Icon, icon_factory


class TaskState(Enum):
    AVAILABLE = 1
    #IN_PROGRESS = 2 # Deprecated.
    SUCCESSFUL = 3
    UNSUCCESSFUL = 4
    CHOSEN = 5
    QUEUED = 6
    ONGOING = 7


class TaskSubcategory(Enum):
    ACTIVE = 1 # Needs to target an event.
    SUPPORT = 2 # Needs to target a team.
    PASSIVE = 3 # Generates an event.


class Task:
    task_counter = 0

    def __init__(self, name: str, description: str, category: str, icons: Dict[Icon, int], wincon: int, losecon: int , subcategory: TaskSubcategory, steps: List[List[Tuple[str, str, str]]] = [("", "", "")], bark_win: str = "", bark_fail: str = "", win_tasks: List[str] = [], lose_tasks: List[str] = []):
        self.name = name
        self.description = description # not really a description, more like the opening bark.
        self.category = category
        self.icons = icons
        self.wincon = wincon
        self.losecon = losecon
        self.bark_win = bark_win
        self.bark_fail = bark_fail
        self.steps = steps # (step, success, failure) -- grab a random list from within, and then get the step.
        self.win_tasks = win_tasks
        self.lose_tasks = lose_tasks
        self.subcategory = subcategory

        self.state: TaskState = TaskState.AVAILABLE
        self.id: int = Task.task_counter
        Task.task_counter += 1
        self.assigned_team_id: int = -1


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
                icons={
                    icon_factory("attack"): 5,
                    icon_factory("defense"): 5,
                },
                wincon=6,
                losecon=4,
                subcategory=TaskSubcategory.ACTIVE,
                
            )
        #
        # SIGINT
        #
        case "sigint_1":
            return Task(
                name="Extraterrestrial Signal Detection and Analysis", 
                description="Scanning frequency bands for unusual signal patterns...", 
                category="sigint",
                icons={
                    icon_factory("observation"): 2,
                    icon_factory("analysis"): 4,
                    icon_factory("deception"): 4,
                },
                wincon=6,
                losecon=4,
                subcategory=TaskSubcategory.PASSIVE,
                win_tasks=["sigint_2", "satcom_1"],
                bark_win="Extraterrestrial signal detection and analysis successful.",
                bark_fail="Reliability compromised: alien signal is lost.",
                steps=
                [
                    [
                        ("Commencing preliminary scans.", 
                            "Slight irregularities in signal background observed.",
                            "No unusual patterns detected. Recalibrating."),
                        ("Begin signal optmization.",
                                "Possible faint anomalies in signal patterns noted.",
                                "Unusual signal interference detected, disrupting initial scans."),
                        ("Refining parameters.",
                                "Alien signal detected, still weak and intermittent.",
                                "Irregularities persist, obscuring further observations."),
                        ("Begin signal analysis via FFT.",
                                "Frequency spectrum dissected; unique spectral patterns identified.",
                                "Analysis setback: FFT algorithm struggles to reveal spectral patterns in the elusive alien transmission."),
                        ("Implementing PCA.",
                                "PCA identified key components.",
                                "PCA challenge: Critical components in the alien transmission elude identification, complicating prioritization."),
                        ("Proritizing data for further analysis.",
                                "Reliable reception of alien communications achieved.",
                                "Parameters adjustment faltering: Alien signal weakens further, intermittent transmission disrupts analysis."),
                    ],
                    [
                        (
                            "Initiating preliminary scans.",
                            "Detecting minor signal background irregularities.",
                            "No unusual patterns detected. Initiating recalibration."
                        ),
                        (
                            "Commencing signal optimization.",
                            "Noticing faint anomalies in signal patterns.",
                            "Signal interference detected, disrupting initial scans."
                        ),
                        (
                            "Fine-tuning signal parameters.",
                            "Detecting intermittent alien signals, still weak.",
                            "Persistent irregularities, hindering further observations."
                        ),
                        (
                            "Starting signal analysis using FFT.",
                            "Dissecting the frequency spectrum, identifying unique patterns.",
                            "FFT analysis facing challenges in revealing spectral patterns in the elusive alien transmission."
                        ),
                        (
                            "Applying PCA for analysis.",
                            "Identifying critical components using PCA.",
                            "PCA encountering difficulties: Critical components in the alien transmission remain elusive, complicating prioritization."
                        ),
                        (
                            "Organizing data for in-depth analysis.",
                            "Achieving stable reception of alien communications.",
                            "Adjusting parameters with difficulties: Alien signal weakening, intermittent transmission disrupting analysis."
                        )
                    ],
                    [
                        (
                            "Initiating preliminary scans.",
                            "Noticing minor signal background irregularities.",
                            "No unusual patterns detected. Starting recalibration."
                        ),
                        (
                            "Commencing signal optimization.",
                            "Observing faint anomalies in signal patterns.",
                            "Signal interference detected, causing disruption in initial scans."
                        ),
                        (
                            "Fine-tuning signal parameters.",
                            "Detecting intermittent alien signals, still weak.",
                            "Persistent irregularities observed, hindering further observations."
                        ),
                        (
                            "Starting signal analysis using FFT.",
                            "Dissecting the frequency spectrum, identifying unique patterns.",
                            "FFT analysis encountering challenges in revealing spectral patterns in the elusive alien transmission."
                        ),
                        (
                            "Applying PCA for analysis.",
                            "Identifying key components using PCA.",
                            "PCA facing challenges: Critical components in the alien transmission remain elusive, complicating prioritization."
                        ),
                        (
                            "Organizing data for in-depth analysis.",
                            "Achieving stable reception of alien communications.",
                            "Struggling with parameter adjustments: Alien signal weakening, intermittent transmission disrupting analysis."
                        )
                    ],
                ]
            )
        case "sigint_2":
            return Task(
                name="Data Mining",
                description="Mining data from alien signal...",
                category="sigint",
                icons={
                    [icon_factory("observation")]: 6,
                },
                wincon=8,
                losecon=4,
                subcategory=TaskSubcategory.ACTIVE,
                bark_win="Valuable insights extracted from alien signal.",
                bark_fail="Unexpected complexities in data hindered our ability to extract meaningful insights. Further analysis and refinement needed.",
                steps=[
                    [
                    ("Initiating data mining process with feature selection and dimensionality reduction.",
                        "Feature selection and dimensionality reduction successful; optimized dataset ready for analysis.",
                        "Challenges encountered during feature selection; refining techniques for improved data reduction."),
                    ("Clustering data points to identify hidden patterns and groups.",
                        "Cluster analysis complete; revealing valuable insights from grouped data points.",
                        "Complex data patterns detected; further analysis needed for precise clustering."),
                    ("Utilizing regression analysis to model relationships and make predictions.",
                        "Regression models successfully developed; accurate predictions derived.",
                        "Regression challenges encountered; refining models for improved predictive performance."),
                    ("Applying classification algorithms to predict categorical outcomes.",
                        "Classification models successfully trained; accurate predictions generated.",
                        "Classification complexities encountered; optimizing models for improved accuracy."),
                    ("Mining sequential patterns to identify temporal trends and behaviors.",
                        "Sequential pattern mining reveals valuable temporal insights.",
                        "Temporal pattern complexities detected; further analysis required for precise trend identification."),
                    ("Leveraging text mining and NLP techniques to extract meaningful insights from unstructured data.",
                        "Text mining and NLP analysis complete; valuable information extracted from textual data.",
                        "NLP complexities encountered; optimizing techniques for improved text analysis."),
                    ("Implementing ensemble methods to enhance model accuracy and robustness.",
                        "Ensemble methods applied successfully; improved model accuracy achieved.",
                        "Ensemble challenges encountered; fine-tuning methods for enhanced model performance."),
                    ("Data preprocessing and cleaning to ensure dataset quality and integrity.",
                        "Data preprocessing complete; clean and well-prepared dataset for mining.",
                        "Data preprocessing challenges encountered; refining techniques for improved data quality."),
                    ],
                ]
                )
        #
        # SATCOM
        #
        case "satcom_1":
            return Task(
                name="Signal Source Tracking",
                description="Positioning satellite arrays for real-time source tracking.",
                category="satcom",
                icons={
                    icon_factory("communication"): 6,
                    icon_factory("jamming"): 2,
                    icon_factory("observation"): 2,
                },
                wincon=6,
                losecon=4,
                subcategory=TaskSubcategory.ACTIVE,
                bark_win="Maintaining situational awareness through the integration of geospatial databases and real-time signal analysis.",
                bark_fail="Unexpected interference disrupted ability to pinpoint the signal source. Further investigation required.",
                steps = [[
                    ("Initiating signal source tracking.",
                        "Tracking process successfully initiated.", 
                        "Failed to initiate tracking process."),
                    ("Configuring satellite array for optimal coverage.", 
                        "Satellite array configuration successful.", 
                        "Configuration failed; readjustment required."),
                    ("Adjusting satellite orbits for continuous coverage.", 
                        "Orbital adjustment completed successfully.", 
                        "Orbital adjustment encountered issues; further adjustments needed."),
                    ("Activating frequency monitoring with adaptive beamforming.", 
                        "Frequency monitoring and beamforming activated.", 
                        "Beamforming challenges; optimizing for reliable data."),
                    ("Performing data correlation with machine learning algorithms.", 
                        "Data correlation and pattern recognition successful.", 
                        "Data correlation complexity; refining for precise results."),
                    ("Establishing real-time tracking using Kalman filtering.", 
                        "Real-time tracking operational with Kalman filtering.", 
                        "Kalman filtering difficulties; recalibrating for improved accuracy."),
                    ("Executing data relay with geospatial data integration.", 
                        "Data relay successfully executed; information transmitted.", 
                        "Integration issues encountered; revising protocols for future attempts."),
                    ("Maintaining continuous monitoring with data fusion.", 
                        "Continuous monitoring ongoing with data fusion.", 
                        "Data fusion complexities; optimizing for seamless collaboration.")
                ],
                ]
            )
        case "real_time_comms":
            return Task(
                name="Real-Time Communications",
                description="Establishing real-time communications with the alien signal source.",
                category="satcom",
                subcategory="support",
                icons={
                    icon_factory("communication"): 6,
                },
                wincon=4,
                win_tasks=["real_time_comms"],
                losecon=99,
                subcategory=TaskSubcategory.SUPPORT,
                bark_win="Real-time communications established with the alien signal source.",
                bark_fail="Unexpected interference disrupted ability to establish real-time communications. Further investigation required.",
                steps = [[
                    ("Initiating real-time communications.",
                        "Real-time communications successfully initiated.",
                        "."),
                    ("Initiating real-time communications. 2",
                        "Real-time communications successfully initiated.",
                        "."),
                    ("Initiating real-time communications. 3",
                        "Real-time communications successfully initiated.",
                        "."),
                    ("Initiating real-time communications. 4",
                        "Real-time communications successfully initiated.",
                        "."),
                ],
                ]
            )