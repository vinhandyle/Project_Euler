# Problem 19: Counting Sundays
# Answer: 171



def run() -> None:
    days = 366
    sundays = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            if days % 7 == 0:
                sundays += 1

            if month == 1:
                days += 31
            elif month == 2:
                if year % 4 == 0:
                    if year % 100 == 0:
                        if year % 400 == 0:
                            days += 29
                        else:
                            days += 28
                    else:
                        days += 29
                else:
                    days += 28
            elif month == 3:
                days += 31
            elif month == 4:
                days += 30
            elif month == 5:
                days += 31
            elif month == 6:
                days += 30
            elif month == 7:
                days += 31
            elif month == 8:
                days += 31
            elif month == 9:
                days += 30
            elif month == 10:
                days += 31
            elif month == 11:
                days += 30
            elif month == 12:
                days += 31

    print(sundays)

    

if __name__ == '__main__':
    run()


