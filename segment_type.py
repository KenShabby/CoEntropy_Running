from enum import Enum


class SegmentType(Enum):
    EASY_RUN = "Easy Run"
    RECOVERY_RUN = "Recovery Run"
    LONG_RUN = "Long Run"
    MEDIUM_LONG_RUN = "Medium Long Run"
    MARATHON_PACE_RUN = "Marathon Pace Run"
    GENERAL_AEROBIC_RUN = "General Aerobic Run"
    LACTATE_THRESHOLD_RUN = "Lactate Threshold Run"
    VO2_MAX_RUN = "VO2 Max Run"
    INTERVALS = "Intervals"

    def __init__(self, type: str):
        self._type = type

    @property
    def description(self) -> str:
        return self._type
