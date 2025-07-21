""" This class is for a full marathon (or other distance plans TBD) plan over
the course of the chosen number of weeks.
"""


class RunningPlan:
    def __init__(self, distance, miles_per_week, weeks, start_date, end_date):
        self.distance = distance
        self.miles_per_week = miles_per_week
        self.weeks = weeks
        self.start_date = start_date
        self.end_date = end_date
        self._days = []

