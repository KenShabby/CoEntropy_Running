"""This class should be able to take a runner's heart rate info, whether it be
Max hr, lactate threshold hr, or heart rate reserve. Then based on the type of
run planned (e.g. recovery run, medium-long run, aerobic run, speedwork) return
a list of heart rate zones.
"""

from hr_zone_methods import HeartRateZoneMethods
from segment_type import SegmentType
import zone_percentages


class RunSegment:
    def __init__(self, name, distance=0, time=0, notes=""):
        self.name = name
        self.distance = distance
        self.duration = time
        self.notes = notes

    def hr_bounds(self):
        if self.name not in SegmentType:
            raise ValueError(f"Unknown segment type: {self.name}")
