from hr_methods import reserve_HR


class RunType:
    def __init__(self, name, notes=""):
        self.name = name
        self.notes = notes
        self.segments = []

    def add_segment(self, run_segment):
        self.segments.append(run_segment)

    def calc_segment_zones(self, segment_name, method=reserve_HR):
        match method:
            case "reserve_HR":
                match segment_name:
                    case "recovery_run":
                        return (50, 70)
                    case "long_run":
                        return (65, 78)
                    case "medium_long_run":
                        return (65, 78)
                    case "marathon_pace_run":
                        return (73, 84)
                    case "general_aerobic_run":
                        return (62, 75)
                    case "lactate_threshold_run":
                        return (77, 88)
                    case "VO2_max_run":
                        return (91, 94)
                    case _:
                        return "I don't recognize that segment type."
            case _:
                return "Method not implemented yet."
