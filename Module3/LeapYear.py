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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
         print("OK")
    else:
         print("Failed")

