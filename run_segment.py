from constants import ZONES_BY_SEGMENT
from hr_methods import reserve_hr

""" This class should be able to take a runner's heart rate info, whether it be
Max hr, lactate threshold hr, or heart rate reserve. Then based on the type of
run planned (e.g. recovery run, medium-long run, aerobic run, speedwork) return
a list of heart rate zones from 1 to 5 with them breaking down like this:
        Zone 1: Low aerobic
        Zone 2: High aerobic
        Zone 3: Tempo
        Zone 4: Threshold
        Zone 5: Anerobic/Max effort
"""


class RunSegment:
    def __init__(self, name, distance, segment_type):
        self.name = name
        self.distance = distance
        self.segment_type = segment_type

    def hr_bounds(self, runner, method=reserve_hr):
        if self.segment_type not in ZONES_BY_SEGMENT:
            raise ValueError(f"Unknown segment type: {self.segment_type}")

        lower_pct, higher_pct = ZONES_BY_SEGMENT[self.segment_type]
        return method(runner, lower_pct, higher_pct)

    def describe(self, runner):
        low, high = self.hr_bounds(runner)
        segment_title = self.name
        segment_type_clean = self.segment_type.replace('_', ' ').title()

        return (
            f"--- {segment_title} ---\n"
            f"Type       : {segment_type_clean}\n"
            f"Distance   : {self.distance:.1f} miles\n"
            f"HR Target  : {low:.0f} – {high:.0f} bpm\n"
        )
