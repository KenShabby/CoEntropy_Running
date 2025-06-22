
# hr_methods.py

def reserve_HR(runner, lower_pct, upper_pct):
    hrr = runner.heart_rate_reserve()
    return (
        round(runner.resting_hr + lower_pct * hrr),
        round(runner.resting_hr + upper_pct * hrr)
    )
