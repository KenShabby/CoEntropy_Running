"""This class should be able to take a runner's heart rate info, whether it be
Max hr, lactate threshold hr, or heart rate reserve. Then based on the type of
run planned (e.g. recovery run, medium-long run, aerobic run, speedwork) return
a list of heart rate zones.
"""

import constants
from segment_type import SegmentType


class RunSegment:
    def __init__(self, runner, name, distance=0, time=0, notes=""):
        self.name = name
        self.distance = distance
        self.duration = time
        self.notes = notes
        self._low_hr_bound
        self._high_hr_bound

    def hr_bounds(self):
        if self.name not in SegmentType:
            raise ValueError(f"Unknown segment type: {self.name}")

        self._low_hr_bound, self._high_hr_bound = constants.HR_ZONE_PERCENTAGES[
            self.name
        ]

    def describe(self):
        low, high = self._low_hr_bound, self._high_hr_bound
        segment_type_clean = self.name.replace("_", " ").title()

        return (
            f"--- Segment ---\n"
            f"Type       : {segment_type_clean}\n"
            f"Distance   : {self.distance:.1f} miles\n"
            f"HR Target  : {low:.0f} – {high:.0f} bpm\n"
        )
