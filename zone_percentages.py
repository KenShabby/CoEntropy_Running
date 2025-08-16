from hr_zone_methods import HeartRateZoneMethods
from typing import Tuple, Dict
from segment_type import SegmentType

HR_ZONE_PERCENTAGES: Dict[
    Tuple[SegmentType, HeartRateZoneMethods], Tuple[float, float]
] = {
    # --- Recovery Run ---
    (SegmentType.RECOVERY_RUN, HeartRateZoneMethods.HR_RESERVE): (0.60, 0.70),
    (SegmentType.RECOVERY_RUN, HeartRateZoneMethods.LTHR): (0.6, 0.85),
    (SegmentType.RECOVERY_RUN, HeartRateZoneMethods.MAX_HR): (0.60, 0.76),
    # --- Long Run ---
    (SegmentType.LONG_RUN, HeartRateZoneMethods.HR_RESERVE): (0.65, 0.78),
    (SegmentType.LONG_RUN, HeartRateZoneMethods.LTHR): (0.84, 0.89),
    (SegmentType.LONG_RUN, HeartRateZoneMethods.MAX_HR): (0.74, 0.84),
    # --- Medium Long Run ---
    (SegmentType.MEDIUM_LONG_RUN, HeartRateZoneMethods.HR_RESERVE): (
        0.65,
        0.78,
    ),
    (SegmentType.MEDIUM_LONG_RUN, HeartRateZoneMethods.LTHR): (
        0.84,
        0.89,
    ),
    (SegmentType.MEDIUM_LONG_RUN, HeartRateZoneMethods.MAX_HR): (
        0.74,
        0.84,
    ),
    # --- Marathon Pace Run ---
    (SegmentType.MARATHON_PACE_RUN, HeartRateZoneMethods.HR_RESERVE): (0.73, 0.84),
    (SegmentType.MARATHON_PACE_RUN, HeartRateZoneMethods.LTHR): (0.85, 0.94),
    (SegmentType.MARATHON_PACE_RUN, HeartRateZoneMethods.MAX_HR): (0.79, 0.88),
    # --- General Aerobic Run ---
    (SegmentType.GENERAL_AEROBIC_RUN, HeartRateZoneMethods.HR_RESERVE): (0.62, 0.75),
    (SegmentType.GENERAL_AEROBIC_RUN, HeartRateZoneMethods.LTHR): (
        0.85,
        0.89,
    ),
    (SegmentType.GENERAL_AEROBIC_RUN, HeartRateZoneMethods.MAX_HR): (0.70, 0.81),
    # --- Lactate Threshold Run  ---
    (SegmentType.LACTATE_THRESHOLD_RUN, HeartRateZoneMethods.HR_RESERVE): (0.77, 0.88),
    (SegmentType.LACTATE_THRESHOLD_RUN, HeartRateZoneMethods.LTHR): (0.94, 0.99),
    (SegmentType.LACTATE_THRESHOLD_RUN, HeartRateZoneMethods.MAX_HR): (0.82, 0.91),
    # --- VO2 Max Run ---
    (SegmentType.VO2_MAX_RUN, HeartRateZoneMethods.HR_RESERVE): (0.91, 0.94),
    (SegmentType.VO2_MAX_RUN, HeartRateZoneMethods.LTHR): (
        1.00,
        1.02,
    ),
    (SegmentType.VO2_MAX_RUN, HeartRateZoneMethods.MAX_HR): (0.93, 0.95),
    # --- Easy Run ---
    (SegmentType.EASY_RUN, HeartRateZoneMethods.MAX_HR): (0.60, 0.70),
    (SegmentType.EASY_RUN, HeartRateZoneMethods.HR_RESERVE): (0.50, 0.60),
    (SegmentType.EASY_RUN, HeartRateZoneMethods.LTHR): (0.70, 0.85),
    # --- Intervals ---
    (SegmentType.INTERVALS, HeartRateZoneMethods.MAX_HR): (0.90, 1.00),
    (SegmentType.INTERVALS, HeartRateZoneMethods.HR_RESERVE): (0.85, 0.95),
    (SegmentType.INTERVALS, HeartRateZoneMethods.LTHR): (1.03, 1.06),
}
