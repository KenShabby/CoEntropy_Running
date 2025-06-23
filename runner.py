class Runner:
    def __init__(self, name="Runner", age=35, maxHR=220, restingHR=50, LTHR=0):
        self.name = name
        self.age = age
        self.maxHR = maxHR or self.estimate_max_hr()
        self.restingHR = restingHR
        self.LTHR = LTHR
        self.heart_rate_reserve = self.calc_HRR()

    def estimate_max_hr(self):
        # Standard max hr formula
        return 220 - self.age

    def calc_HRR(self):
        return self.maxHR - self.restingHR

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"
