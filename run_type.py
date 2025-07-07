"""
This is the top-level run class. It holds the collection of different segments
whether they be warm-up/cool-down, long-run, or a interval/rest sequence.
"""

from hr_methods import reserve_hr
from constants import HRR_ZONES_BY_SEGMENT
from run_segment import RunSegment


class RunType:
    def __init__(self, name, notes=""):
        self.name = name
        self.notes = notes
        self.segments = []

    def add_segment(self, run_segment):
        self.segments.append(run_segment)

    def remove_segment(self) -> RunSegment:
        return self.segments.pop()

    def calc_segment_zones(self, segment_name, method=reserve_hr):
        if method != reserve_hr:
            raise ValueError("Only reserve heart rate zones are implemented so far.")

        try:
            lower_pct, higher_pct = HRR_ZONES_BY_SEGMENT[segment_name]
            return method(lower_pct, higher_pct)
        except KeyError:
            raise ValueError(f"Unknown segment type: {segment_name}")
