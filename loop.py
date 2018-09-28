Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Solution


def is_leap(year):
    leap = False
    if year%400==0:
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    
    return leap


year = int(raw_input())
print is_leap(year)