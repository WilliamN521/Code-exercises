# Function
def ClockConversion(s):
    # 12:00:00AM is 00:00:00 on a 24-hour clock.
    # 12:00:00PM 12:00:00 on a 24-hour clock.
    # hour clock format hh:mm:ssAM or hh:mm:ssPM
    schedule = s[-2:]
    result = ""
    conversion_pm = {"01": "13", "02": "14", "03": "15", "04": "16",
                     "05": "17", "06": "18", "07": "19", "08": "20",
                     "09": "21", "10": "22", "11": "23", "12": "12"}
    nums = s[:2]
    if schedule == "PM":
        if nums in conversion_pm:
            result = conversion_pm[nums]+s[2:8]
    else:
        if nums == "12":
            result = "00"+s[2:8]
        else:
            result = s[:8]

    return result


# Execution
if __name__ == '__main__':
    # Test cases
    s = "12:05:45AM"
    s2 = "12:53:12PM"
    s3 = "06:40:03AM"

    # function call
    print(f"\nResult: {ClockConversion(s)}")
    print(f"\nResult: {ClockConversion(s2)}")
    print(f"\nResult: {ClockConversion(s3)}")