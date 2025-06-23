from hr_methods import reserve_hr
from run_segment import RunSegment


class IntervalSegment(RunSegment):
    def __init__(self, effort_name, reps, effort_pct, rest_pct,
                 effort_duration, rest_duration):
        super().__init__(effort_name, reps * (effort_duration + rest_duration),
                         effort_pct, effort_pct)
        self.reps = reps
        self.effort_duration = effort_duration
        self.rest_duration = rest_duration
        self.rest_pct = rest_pct

    def describe(self, runner):
        effort_low, effort_high = self.hr_bounds(runner)
        rest_low, rest_high = reserve_hr(
            runner, self.rest_pct, self.rest_pct)
        return (f"{self.effort_name}: {self.reps} x {self.effort_duration} min at \
                {effort_low}-{effort_high} bpm, with {self.rest_duration} min \
                rest at {rest_low}-{rest_high} bpm")
