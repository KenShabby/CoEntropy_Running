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
        self._low_hr_bound = 0
        self._high_hr_bound = 0

    def hr_bounds(self):
        if self.name not in SegmentType:
            raise ValueError(f"Unknown segment type: {self.name}")

        bounds_tuple = zone_percentages.HR_ZONE_PERCENTAGES[
            (self.name, HeartRateZoneMethods.MAX_HR)
        ]
        print(f"Bounds tuple: {bounds_tuple}")

        self._low_hr_bound, self._high_hr_bound = bounds_tuple[0], bounds_tuple[1]

    def describe(self):
        low, high = self._low_hr_bound, self._high_hr_bound
        segment_type_clean = self.name.replace("_", " ").title()

        return (
            f"--- Segment ---\n"
            f"Type       : {segment_type_clean}\n"
            f"Distance   : {self.distance:.1f} miles\n"
            f"HR Target  : {low:.0f} – {high:.0f} bpm\n"
        )
