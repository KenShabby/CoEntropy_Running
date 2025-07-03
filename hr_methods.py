# hr_methods.py


def reserve_hr(runner, lower_pct, upper_pct):
    hrr = runner.calc_hrr()
    return (
        round(runner.resting_hr + lower_pct * hrr),
        round(runner.resting_hr + upper_pct * hrr),
    )


def lthr(runner, lower_pct, upper_pct): ...
