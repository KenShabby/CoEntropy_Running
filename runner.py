
class Runner:
    def __init__(self, name="Runner", age=35, maxHR=None, restingHR=None, LTHR=0):
        self.name = name
        self.age = age
        self.maxHR = maxHR or self.estimate_max_hr()
        self.restingHR = restingHR
        self.LTHR = LTHR

    def estimate_max_hr(self):
        # Standard max hr formula
        return 220 - self.age

    def calc_HRR(self):
        return self.maxHR - self.restingHR
