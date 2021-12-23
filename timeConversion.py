# Given a time in 12 hour AM/PM format, convert it to military (24-hour) time.
# Example s = '12:01:00AM' returns '00:01:00'


def timeConversion(s):
    if s[:2] == "12" and s[-2:] == "AM": # if time is midnight
        return "00" + s[2:8]

    elif (s[-2:] == "AM") or (s[:2] == "12" and s [-2:] == "PM"): # if time is AM or noon
        return s[:-2]
    
        
    else:
        return (str(int(s[:2]) + 12)) + s[2:-2] # if time is PM and not any of the above special cases
