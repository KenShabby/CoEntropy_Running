"""
This is the top-level run class. It holds the collection of different segments
whether they be warm-up/cool-down, long-run, or a interval/rest sequence.
"""

from dataclasses import dataclass
from run_segment import RunSegment
import constants
from runner import Runner
from typing import List


@dataclass
class Run:
    runner: Runner
    segments: List[RunSegment]

    def add_segment(self, run_segment):
        self.segments.append(run_segment)

    def remove_segment(self) -> RunSegment:
        return self.segments.pop()

    def get_run_summary(self) -> str:
        summary = f"Run Summary for {self.runner}\n"
        summary += f"Using HR Method: {self.runner.hr_method.value}\n"
        summary += "---------------------------------------\n"
        for i, segment in enumerate(self.segments):
            lower_hr, upper_hr = self.runner.calculate_segment_hr_range(segment.name)

            summary += f"Segment {i + 1}: {segment.name.description} - Duration: {segment.duration}"
            if segment.distance:
                summary += f", Distance: {segment.distance:.2f} km"
            summary += (
                f", Target HR: {lower_hr}-{upper_hr} bpm"  # Display calculated HR range
            )
            if segment.notes:
                summary += f", Notes: {segment.notes}"
            summary += "\n"

        return summary
