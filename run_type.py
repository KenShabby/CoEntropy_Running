class RunType:
    def __init__(self, name, notes=""):
        self.name = name
        self.notes = notes
        self.segments = []

    def add_segment(self, run_segment):
        self.segments.append(run_segment)
