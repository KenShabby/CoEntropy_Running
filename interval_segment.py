""" This class is for run segments that have sprint/recover repeats. For example,
the runner might run 1 km at their 5K pace and then spend a couple of minutes
recovering at an easy pace. Then this process repeats, typically 5 to 10 times.
"""

from hr_methods import reserve_hr
from run_segment import RunSegment


class IntervalSegment(RunSegment):
    def __init__(
        self,
        name,
        distance,
        segment_type,
        effort_name,
        effort_duration,
        rest_duration,
        reps,
    ):
        super().__init__(name, distance, segment_type)
        self.effort_name = effort_name
        self.effort_duration = effort_duration
        self.rest_duration = rest_duration
        self.reps = reps

    def describe(self, runner):
        effort_low, effort_high = self.hr_bounds(runner)
        return f"{self.effort_name}: {self.reps} x {self.effort_duration} min at \
                {effort_low}-{effort_high} bpm, with {self.rest_duration} min \
                rest"
