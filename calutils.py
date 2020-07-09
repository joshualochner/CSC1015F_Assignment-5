from math import ceil

def is_leap_year(year):
    return (year%400 == 0) or ((year%4 == 0 ) and (year%100 != 0))
    
def month_name(number):
    return ['January','February','March','April','May','June','July','August','September','October','November','December'][number-1]
    
def days_in_month(month_number, year):
    if(month_number in [1,3,5,7,8,10,12]):
        return 31
    elif (month_number in [4,6,9,11]):
        return 30
    else:
        if is_leap_year(year):
            return 29
        else:
            return 28
        

def first_day_of_year(year):
    return (1+(5*((year-1)%4))+(4*((year-1)%100))+(6*((year-1)%400)))%7

def first_day_of_month(month_number, year):
    a = (month_number - 3)%12+1
    m = ceil(2.6*a)%7
    if(a in [11,12]):
        m-=1
    elif is_leap_year(year):
        m+=1
    return (1+m+(5*((year-1)%4))+(4*((year-1)%100))+(6*((year-1)%400)))%7