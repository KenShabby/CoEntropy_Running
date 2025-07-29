import hr_zone_methods
from runner import Runner
import menus
import sys


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
            brendan = Runner(49, hr_zone_methods.MAX_HR, 0, 0, 0, maxHR)
        case "2":  # HRR Calculation
            hr_max, hr_min = menus.hrr_zone_menu()
            brendan = Runner(49, hr_zone_methods.HR_RESERVE, hr_min, 0, 0, hr_max)
        case "3":  # LTHR Calculation
            lthr = menus.lthr_menu()
            brendna = Runner(49, hr_zone_methods.LTHR, 0, lthr)
        case "q":  # Quit
            sys.exit()
        case _:
            print("invalid choice")
            menus.hr_zone_menu()


if __name__ == "__main__":
    main()
