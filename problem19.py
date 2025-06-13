# Counting Sundays

def is_leap_year(check_year):
    if check_year % 4 == 0 and year % 100 > 0:
        return True
    elif check_year % 400 ==0:
        return True

    return False


def counting_sundays(sunday_date, curr_year):
    months = [31, 29 if is_leap_year(curr_year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    no_of_sundays_on_1st = 0
    for curr_month in range(12):
        curr_months_sunday = sunday_date
        while curr_months_sunday < months[curr_month]:
            sunday_date = (sunday_date + 7) % months[curr_month]
            if sunday_date == 1:
                no_of_sundays_on_1st+=1
            curr_months_sunday += 7

    return sunday_date, no_of_sundays_on_1st

total_no_of_sundays = 0
first_sunday_date = 6 # date of the first sunday in the year 1901 january

for year in range(1901, 2001):
    next_year_sunday_date, no_of_sundays = counting_sundays(first_sunday_date, year)

    first_sunday_date = next_year_sunday_date
    total_no_of_sundays += no_of_sundays

print(total_no_of_sundays)
