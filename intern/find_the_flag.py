filename = input('Filename: ')
lines = open(filename, 'r').read()
flag = input('Flag: ')
for line in lines:
    if line == flag:
        print('line')
    else:
        print("aaaa")