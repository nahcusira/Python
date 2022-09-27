while True:
    d = input("Enter a day: ")
    try:
        day = int(d)
    except:
        print("Day must be integer.")
        continue
    if day < 0:
        print("Day must be positive integer.")
        continue
    while True:
        m = input("Enter a month: ")
        try:
            month = int(m)
        except:
            print("Month must be integer.")
            continue
        if month < 0:
            print("Month must be positive integer")
            continue
        while True:
            y = input("Enter a year: ")
            try:
                year = int(y)
            except:
                print("Year must be integer.")
                continue
            if year < 0:
                print("Year must be positive integer")
                continue
            else:
                if ((year % 400) == 0 or (year % 4 == 0 and year % 100 != 0)) and day <= 29:
                    print("Valid day.")
                else:
                    print("Invalid day.")
                break
        break
    continue
