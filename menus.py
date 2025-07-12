
def main_menu():
    print("""
        *** MENU ***
        1. Calculate heart rate zones
        2. Plan a run

        Q. Exit
        """)

    return input("Enter your choice: ")

def hr_zone_menu():
    print("""
        *** Enter a heart rate calculation method ***

        1. Max heart rate
        2. Heart rate reserve
        3. Lactate threshold heart rate

        Q. Exit
        """)

    return input("Enter your choice: ")

def max_hr_zone_menu():
    ...

def hrr_zone_menu():
    max_hr = input("Enter Max HR: ")  
    rest_hr = input("Enter resting HR: ")
    runner = Runner("Runner", 49, max_hr, rest_hr, 0)
    return runner

def lthr_menu():
    ...

