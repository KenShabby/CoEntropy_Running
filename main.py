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

    def do_max(self, line: str):
        """Calculate max heart rate zones"""
        maxHR = int(menus.max_hr_zone_menu())
        brendan = Runner("Brendan", 49, HeartRateZoneMethods.MAX_HR, 0, 0, 0, maxHR)
        my_run = Run(brendan, [])

    def do_hrr(self, line: str):
        """Calculate heart rate reserver zones"""
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

    def do_lthr(self, line: str):
        """Calculate lactate threshold heart rate zones"""
        menus.lthr_menu()


def main():
    """Entry point for the REPL application"""
    try:
        REPL().cmdloop()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)


def build_run(run: Runner):
    pass


if __name__ == "__main__":
    main()
"""
        case "3":  # LTHR Calculation
            lthr = menus.lthr_menu()
            brendan = Runner("Brendan", 49, HeartRateZoneMethods.LTHR, 0, int(lthr))
        case "q":  # Quit
            sys.exit()
        case _:
            print("invalid choice")
            menus.hr_zone_menu()

    # Create a run

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
