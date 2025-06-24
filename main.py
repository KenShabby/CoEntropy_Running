from hr_methods import reserve_hr
from run_segment import RunSegment
from run_type import RunType
from runner import Runner


def main():

    brendan = Runner(
        name="Brendan",
        age=49,
        max_hr=174,
        resting_hr=53,
        lthr=157
    )

    tuesday_run = RunType(
        name="general_aerobic_run",
        notes="Will probably have to postpone due to calf pull."
    )

    segment = RunSegment(
        name="9 mile recovery run",
        distance=9.0,
        segment_type="general_aerobic_run"
    )

    tuesday_run.add_segment(segment)

    # Print the run description
    for segment in tuesday_run.segments:
        print(tuesday_run.notes)
        print(segment.describe(brendan))


if __name__ == "__main__":
    main()
