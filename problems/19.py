
months = {
    1:31, 2:28, 3:31, 4:30,
    5:31, 6:30, 7:31, 8:31,
    9:30, 10:31, 11:30, 12:31
}

days_rem = 3
sundays = 0
for year in range(1901,2001):
    for month in range(1,13):
        if year == 1901 and month == 1:
            continue
        days_rem += months[month]
        if month==2 and (year%4 == 0 and year%400 != 0):
            days_rem += 1

        days_rem = days_rem % 7
        if days_rem == 0:
            sundays += 1

print(sundays)