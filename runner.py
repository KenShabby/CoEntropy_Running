"""
This class keeps track of the individual's name, age, and heart rate stats.
"""

class Runner:
    def __init__(self, age, max_hr, resting_hr, lthr):
        self.age = age
        self.max_hr = max_hr or self.estimate_max_hr()
        self.resting_hr = resting_hr
        self.lthr = lthr
        self.hr_reserve = self.calc_hrr()

    def estimate_max_hr(self):
        # Standard way to estimate maximum heart rate
        return 220 - self.age

    def calc_hrr(self):
        return self.max_hr - self.resting_hr

    def __repr__(self):
        return f"Age: {self.age}, Max HR: {self.max_hr}, Resting HR: \
                {self.resting_hr}, Lactate Threshold HR: {self.lthr}"
