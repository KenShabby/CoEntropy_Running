class Runner:
    def __init__(self, name, age, max_hr, resting_hr, lthr):
        self.name = name
        self.age = age
        self.max_hr = max_hr or self.estimate_max_hr()
        self.resting_hr = resting_hr
        self.lthr = lthr
        self.hr_reserve = self.calc_hrr()

    def estimate_max_hr(self):
        # Standard max hr formula
        return 220 - self.age

    def calc_hrr(self):
        return self.max_hr - self.resting_hr

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"
