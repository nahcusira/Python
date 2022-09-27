def checkInput1():
    while True:
        try:
            num = int(input('Enter the integral part: '))
            return num
        except ValueError:
            print('The integral part must be integer.')
def checkInput2():
    while True:
        try:
            frac = int(input('Enter the fraction: '))
            if frac < 0.0 :
                print('The fraction must be positive.')
                pass
            else:
                return frac
        except ValueError:
            print('The fraction must be integer')

num = checkInput1()
frac = checkInput2()
print('Real number: ', num,'.',frac, sep='' )

