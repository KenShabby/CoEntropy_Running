from hr_methods import reserve_hr
from run_segment import RunSegment
from run_type import RunType
from runner import Runner


def main():

    brendan = Runner(
        name="Brendan",
        age=49,
        max_hr=174,
        resting_hr=53
    )

    recovery = RunType(
        name="recovery_run",
        notes="Easy run after a hamstring pull."
    )

    segment = RunSegment(
        name="10 mile recovery run",
        distance=10.0,
        segment_type="recovery_run"
    )

    recovery.add_segment(segment)

    # Print the run description
    for segment in recovery.segments:
        print(segment.describe(brendan))


if __name__ == "__main__":
    main()
