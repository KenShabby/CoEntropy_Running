"""
This class keeps track of the individual's name, age, and heart rate stats.
"""

from zone_percentages import HR_ZONE_PERCENTAGES
from run_segment import SegmentType
from typing import Tuple
from dataclasses import dataclass
from hr_zone_methods import HeartRateZoneMethods


@dataclass
class Runner:
    name: str
    age: int
    hr_method: HeartRateZoneMethods
    resting_hr: int = 0
    lthr: int = 0
    hrr: int = 0
    max_hr: int = 0

    def __post_init__(self):
        if self.max_hr == 0:
            self.max_hr = 220 - self.age

        if self.hr_method == HeartRateZoneMethods.HR_RESERVE and self.resting_hr == 0:
            raise Exception(
                "You must supply a resting heart rate to use reserve hr method."
            )
        else:
            self.hrr = self.max_hr - self.resting_hr

        if self.hr_method == HeartRateZoneMethods.LTHR and self.lthr == 0:
            raise Exception(
                "You must supply a lactate threshhold heart rate\
                    to use lthr method."
            )

    def get_base_hr(self) -> int:
        """Returns the base heart rate value for the chosen method."""
        if self.hr_method == HeartRateZoneMethods.MAX_HR:
            return self.max_hr
        elif self.hr_method == HeartRateZoneMethods.HR_RESERVE:
            return self.max_hr - self.resting_hr
        elif self.hr_method == HeartRateZoneMethods.LTHR:
            return self.lthr
        else:
            raise ValueError("Unsupported heart rate method.")

    def calculate_segment_hr_range(self, segment_type: SegmentType) -> Tuple[int, int]:
        """
        Calculates the target lower and upper heart rate for a given segment type
        based on the runner's chosen HR method and the defined percentages.
        """
        key = (segment_type, self.hr_method)
        if key not in HR_ZONE_PERCENTAGES:
            # Fallback or raise an error if a combination isn't defined
            print(
                f"Warning: HR percentages not defined for {segment_type.description} with {self.hr_method.value}. Returning (0, 0)."
            )
            return (0, 0)

        lower_percent, upper_percent = HR_ZONE_PERCENTAGES[key]
        base_hr = self.get_base_hr()

        lower_hr = int(base_hr * lower_percent)
        upper_hr = int(base_hr * upper_percent)

        # For HR_RESERVE method, you add resting HR back to the calculated values
        if self.hr_method == HeartRateZoneMethods.HR_RESERVE:
            lower_hr += self.resting_hr
            upper_hr += self.resting_hr

        return (lower_hr, upper_hr)

    def __repr__(self):
        return f"Age: {self.age}, Heart Rate Calculation Method: {self.hr_method}, Max HR: {self.max_hr}, Resting HR: {self.resting_hr}, HR Reserve: {self.hrr}, Lactate Threshold HR: {self.lthr}"
