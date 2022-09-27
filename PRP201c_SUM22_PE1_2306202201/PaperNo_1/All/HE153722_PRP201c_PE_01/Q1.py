try:
    day = int(input('Enter a day: '))
    month = int(input('Enter a month: '))
    year = int(input('Enter a year: '))
    if day < 1 or day > 31 or month < 1 or month > 12 or year < 1:
        print('Invalid day.')
    elif year % 400 == 0:
        if month == 2:
            if 0 < day <= 29:
                print('Valid day.')
            else:
                print('Invalid day.')
        if (0 < month <= 12):
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 0 < day <= 31:
                    print('Valid day.')
                else:
                    print('Invalid day.')
        if month > 12 or month <= 0:
            print('Invalid day.')
        if (0 < month <= 12):
            if month == 4 or month == 6 or month == 9 or month == 11:
                if 0 < day <= 30:
                    print('Valid day.')
                else:
                    print('Invalid day.')
    else:
        if month == 2:
            if 0 < day <= 28:
                print('Valid day.')
            else:
                print('Invalid day.')
        if (0 < month <= 12):
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 0 < day <= 31:
                    print('Valid day.')
                else:
                    print('Invalid day.')
        if month > 12 or month < 0:
            print('Invalid day.')
        if (0 < month <= 12):
            if month == 4 or month == 6 or month == 9 or month == 11:
                if 0 < day <= 30:
                    print('Valid day.')
                else:
                    print('Invalid day.')
except Exception as e:
    print(e)