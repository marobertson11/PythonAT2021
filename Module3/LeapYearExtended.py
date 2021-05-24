def is_year_leap(year):
    '''
    Leap Years are any year that can be exactly divided by 4 (such as 2016, 2020, 2024, etc)
    ^^^ If block 1

    except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
    ^^^ If block 2

    except if it can be exactly divided by 400, then it is (such as 2000, 2400)
    ^^^ If block 3
    '''
    if year % 4 == 0: 
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    else:
        return False

def days_in_month(year, month):
    # Find out why a dict does not work here
    breakpoint()
    d30 = [4, 6, 9, 11]
    d31 = [1, 3, 5, 7, 8, 10, 12]

    if month in d30:
        return 30
    elif month in d31:
        return 31
    # this leap does not make sense
    # TODO Verify logic is correct.
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
