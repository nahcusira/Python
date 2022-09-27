def valid():
    while True:
        try:
            num = int(input(''))
            if num < 0:
                print('the number must be a positive number.')
                continue
            return num
        except ValueError:
            print('the number must be a positive number.')