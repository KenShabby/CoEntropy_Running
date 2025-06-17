class TrainingPace:
    def __init__(self, maxHR, restingHR):
        self.maxHR = maxHR
        self.restingHR = restingHR

    def calc_recovery_pace(self, heart_rate):

