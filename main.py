from constants import HRR_ZONES_BY_SEGMENT
from hr_methods import reserve_hr
from run_segment import RunSegment
from run_type import RunType
from runner import Runner

def main():

    # age = input("Enter your age: ")
    max_hr = int(input("Enter your maximum heart rate: "))
    resting_hr = int(input("Enter your resting heart rate: "))
    # run_type = input("Enter the run type you're planning: ")

    # For the initial stage of the app, we can just have the app print a table
    # of heart rate zones for all potential runs. We'll state with HRR calculations.

    brendan = Runner(
        name="Brendan",
        age=49,
        max_hr = max_hr,
        resting_hr = resting_hr,
        lthr=157
    )

    
    run = RunType(
        name = "",
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
