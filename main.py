from hr_zone_methods import HeartRateZoneMethods
from run import Run
from run_segment import RunSegment
from runner import Runner
from segment_type import SegmentType
import menus
import sys
import cmd


class REPL(cmd.Cmd):
    """A test REPL for my running heart rate calculator."""

    intro = "Welcome to CoEntropy Running! Type Help for commands.\n"
    prompt = " CoEntropy Running > "

    def __init__(self):
        super().__init__()

    def do_max_heart_rate(self):
        """Calculate max heart rate zones"""
        pass

    def do_hrr_heart_rate(self):
        """Calculate heart rate reserver zones"""
        pass

    def do_lthr_heart_rate(self):
        """Calculate lactate threshold heart rate zones"""
        pass


def main():
    """Entry point for the REPL application"""
    try:
        REPL().cmdloop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
"""
def main():
    choice = menus.main_menu()

    # For the initial stage of the app, we can just have the app print a table
    # of heart rate zones for all potential runs. We'll state with HRR calculations.

    match choice.lower():
        case "1":  # Calculate HR Zones
            choice = menus.hr_zone_menu()
        case "2":  # Plan a run
            choice = menus.run_plan_menu()
        case "q":
            print("Exiting!")
            sys.exit()
        case _:
            print("Invalid choice")

    match choice.lower():
        case "1":  # Max Heart Rate Calculation
            maxHR = int(menus.max_hr_zone_menu())
            brendan = Runner("Brendan", 49, HeartRateZoneMethods.MAX_HR, 0, 0, 0, maxHR)
        case "2":  # HRR Calculation
            hr_max, hr_min = menus.hrr_zone_menu()
            brendan = Runner(
                "Brendan",
                49,
                HeartRateZoneMethods.HR_RESERVE,
                int(hr_min),
                0,
                0,
                int(hr_max),
            )
        case "3":  # LTHR Calculation
            lthr = menus.lthr_menu()
            brendan = Runner("Brendan", 49, HeartRateZoneMethods.LTHR, 0, int(lthr))
        case "q":  # Quit
            sys.exit()
        case _:
            print("invalid choice")
            menus.hr_zone_menu()

    # Create a run
    my_run = Run(brendan, [])

    long_run_segment = RunSegment(SegmentType.LONG_RUN, 1)
    long_run_segment.hr_bounds()
    my_run.add_segment(long_run_segment)

    recovery_run_segment = RunSegment(SegmentType.RECOVERY_RUN, 1)
    recovery_run_segment.hr_bounds()
    my_run.add_segment(recovery_run_segment)

    medium_long_run_segment = RunSegment(SegmentType.MEDIUM_LONG_RUN, 1)
    medium_long_run_segment.hr_bounds()
    my_run.add_segment(medium_long_run_segment)

    print(my_run.get_run_summary())
"""
