""" This class should be able to take a runner's heart rate info, whether it be
Max hr, lactate threshold hr, or heart rate reserve. Then based on the type of
run planned (e.g. recovery run, medium-long run, aerobic run, speedwork) return
a list of heart rate zones.
"""

from hr_methods import reserve_hr
from constants import *


class RunSegment:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def hr_bounds(self, runner, method=reserve_hr):
        if self.name not in HRR_ZONES_BY_SEGMENT:
            raise ValueError(f"Unknown segment type: {self.name}")

        lower_pct, higher_pct = HRR_ZONES_BY_SEGMENT[self.name]
        return method(runner, lower_pct, higher_pct)

    def describe(self, runner):
        low, high = self.hr_bounds(runner)
        segment_title = self.name
        segment_type_clean = self.name.replace('_', ' ').title()

        return (
            f"--- {segment_title} ---\n"
            f"Type       : {segment_type_clean}\n"
            f"Distance   : {self.distance:.1f} miles\n"
            f"HR Target  : {low:.0f} – {high:.0f} bpm\n"
        )
