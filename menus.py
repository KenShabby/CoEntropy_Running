def max_hr_zone_menu():
    known = input("Do you know your maximum heart rate? (y/n): ")
    if known.lower() == "y":
        maxHR = input("What is your max HR: ")
    else:
        age = int(input("What is your age: "))
        maxHR = 220 - age
        print(f"We'll use {maxHR} beats per minute as an estimate.")
    return maxHR


def hrr_zone_menu():
    max_hr = input("Enter Max HR: ")
    rest_hr = input("Enter resting HR: ")
    return max_hr, rest_hr
