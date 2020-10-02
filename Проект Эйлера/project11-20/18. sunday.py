def cycle_week(week: list, numbers):
    if numbers == 31:
        for _ in range(3):
            tmp = week[0]
            for i in range(len(week) - 1):
                week[i] = week[i + 1]
            week[len(week) - 1] = tmp

    elif numbers == 30:
        for _ in range(2):
            tmp = week[0]
            for i in range(len(week) - 1):
                week[i] = week[i + 1]
            week[len(week) - 1] = tmp

    elif numbers == 29:
        tmp = week[0]
        for i in range(len(week) - 1):
            week[i] = week[i + 1]
        week[len(week) - 1] = tmp

    elif numbers == 28:
        return week


week = [2, 3, 4, 5, 6, 7, 1]  # 01/01/19001 - Tuesday - 2. sunday - 7

d = {'sunday': 0}  # if week[0] = 7 ---> d['sunday'] +=1

lst_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

lst_classic = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for n in range(1901, 2001):

    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                day_in_year = 366
            else:
                day_in_year = 365
        else:
            day_in_year = 366
    else:
        day_in_year = 365

    if day_in_year == 365:
        for month in lst_classic:
            cycle_week(week, month)

            if week[0] == 7:
                d['sunday'] += 1

    if day_in_year == 366:
        for month in lst_leap:
            cycle_week(week, month)

            if week[0] == 7:
                d['sunday'] += 1
print(d)
