while True:
    a = input("Enter the integral part: ")
    try:
        number1 = int(a)
    except:
        print("The integral part must be number.")
        continue
    while True:
        b = input("Enter the fraction: ")
        try:
            number2 = int(b)
        except:
            print("The fraction must be number.")
            continue
        if number2 < 0:
            print("The fraction must be positive integer")
            continue
        else:
            print("Real number: " + str(number1) + "." + str(number2))

