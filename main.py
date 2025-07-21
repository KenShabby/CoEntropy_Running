from constants import *
from run_segment import RunSegment
from run_type import RunType
from runner import Runner
import menus
import sys

def main():

    choice = menus.main_menu()

    # For the initial stage of the app, we can just have the app print a table
    # of heart rate zones for all potential runs. We'll state with HRR calculations.

    match choice.lower():
        case "1": # Calculate HR Zones
            choice = menus.hr_zone_menu()
        case "2": # Plan a run
            choice = menus.run_plan_menu()
        case "q":
            print("Exiting!")
            sys.exit()
        case _:
            print("Invalid choice")

    match choice.lower():
        case "1": # Max Heart Rate Calculation
            maxHR = int(menus.max_hr_zone_menu())
            print_runner_zones("MAX_HR_ZONES_BY_SEGMENT", maxHR)
        case "2": # HRR Calculation
            hrr = menus.hrr_zone_menu()
            print_runner_zones("HRR_ZONES_BY_SEGMENT", hrr)
        case "3": # LTHR Calculation
            lthr = menus.lthr_menu()
            print_runner_zones("LTHR_ZONES_BY_SEGMENT", lthr)
        case "q": # Quit
            sys.exit()
        case _:
            print("invalid choice")
            menus.hr_zone_menu()

def print_runner_zones(heart_rate_type, base_rate):

    match heart_rate_type:
        case "MAX_HR_ZONES_BY_SEGMENT":
            runner = Runner("Runner", 35, base_rate, 0, 0)
        case "HRR_ZONES_BY_SEGMENT":
            runner = Runner("Runner", 35, 0, base_rate, 0)
        case "LTHR_ZONES_BY_SEGMENT":
            runner = Runner("Runner", 35, 0, 0, base_rate)

    run = RunType(
        name = "All run types",
        notes = ""
    )

    for segment in HRR_ZONES_BY_SEGMENT:
        temp = RunSegment(
            name = segment,
            distance = 1.0,
            segment_type = segment
        )
        run.add_segment(temp)

    # Print the run description
    for segment in run.segments:
        print(run.notes)
        print(segment.describe(runner))

if __name__ == "__main__":
    main()
