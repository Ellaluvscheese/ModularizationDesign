# 1. Name:
#      Ella Galbraith
# 2. Assignment Name:
#      Lab 03 : Calendar Program
# 3. Assignment Description:
#      This program gets user input for the year and then the month and then displays the month in a calendar type view.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part if this assignment was the days since function because I kept forgetting small math details haha.
# 5. How long did it take for you to complete the assignment?
#      It took me about 2.5 hours to complete this assignment

def main():
    year = get_year()
    month = get_month()
    leap_check = check_leap(year)
    month_days_count = jan_to_cur_month_count(month, leap_check)
    years = years_since(year)
    day_num = days_since(years, month_days_count)
    dow = day_of_week(day_num)

    # fix the month day count thing lol
    display_table(dow, month_day_count(month, leap_check))


    

def get_year():
    try:
       year = int(input("What is the year you want?: "))
       if year >= 1753:
           return year
       else: 
           print("Invalid year. ")
    except ValueError:
        return "Invalid year. "

def get_month():
    try:
       month = int(input("What is the month you want?(1-12): "))
       if 1 <= month <= 12:
           return month
       else: 
           print("Invalid month. ")
    except ValueError:
        return "Invalid month. "

def check_leap(year):
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True
    else:
        leap = False
    return leap

def month_day_count(user_month, leap_year):
    if user_month == 1 or user_month == 3 or user_month == 5 or user_month == 7 or user_month == 8 or user_month == 10 or user_month == 12:
        days = 31
    if user_month == 4 or user_month == 6 or user_month == 9 or user_month == 11:
        days = 30
    if user_month == 2 and leap_year:
        days = 29
    if user_month == 2 and not leap_year:
        days = 28
    
    return days
    
def jan_to_cur_month_count(user_month, leap_year):
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year:
        month_days[1] = 28
    index = user_month - 1
    sum_days = 0
    for i in range(index):
        sum_days = sum_days + month_days[i]
    return sum_days


def years_since(user_year):
    return user_year - 1753

def days_since(years_since, month_day_count):
    leap_year_number = years_since // 4
    non_leap = years_since - leap_year_number
    non_days = non_leap * 365
    leap_days = leap_year_number * 366
    days = non_days + leap_days
    days_fr = days + month_day_count
    return days_fr

def day_of_week(days_since):
    day = days_since % 7
    return day


def display_table(dow, num_days):
    '''Display a calendar table'''
    assert(type(num_days) == type(dow) == type(0))
    assert(0 <= dow <= 6)
    assert(28 <= num_days <= 31)

    # Display a nice table header
    print("  Su  Mo  Tu  We  Th  Fr  Sa")

    # Indent for the first day of the week
    for indent in range(dow):
        print("    ", end='')

    # Display the days of the month
    for dom in range(1, num_days + 1):
        print(repr(dom).rjust(4), end='')
        
        # Newline after Saturdays
        if (dom + dow) % 7 == 0:
            print("") # newline

    # We must end with a newline
    if (num_days + dow) % 7 != 0:
        print("") # newline


# Output
#display_table(3, 31)
main()