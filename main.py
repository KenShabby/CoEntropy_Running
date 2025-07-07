from constants import HRR_ZONES_BY_SEGMENT
from hr_methods import reserve_hr
from menu import print_menu
from run_segment import RunSegment
from run_type import RunType
from runner import Runner
import sys

def main():

    choice = print_menu()

    # For the initial stage of the app, we can just have the app print a table
    # of heart rate zones for all potential runs. We'll state with HRR calculations.

    match choice.lower():
        case "1":
            print_runner_zones()
        case "2":
            print("You chose 2")
        case "q":
            sys.exit()
        case _:
            print("Invalid choice")


def print_runner_zones():

    brendan = Runner("Brendan", 49, 174, 56, 157)

    run = RunType(
        name = "All run types",
        notes = ""
    )

    for segment in HRR_ZONES_BY_SEGMENT:
        temp = RunSegment(
            name = "",
            distance = 1.0,
            segment_type = segment
        )
        run.add_segment(temp)

    # Print the run description
    for segment in run.segments:
        print(run.notes)
        print(segment.describe(brendan))

if __name__ == "__main__":
    main()
