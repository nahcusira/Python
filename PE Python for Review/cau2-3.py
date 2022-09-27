try:
    fname = input('Enter the file name: ')
    if not fname:
        fname = 'Trace.txt'
    f= open(fname,'r')
    lines = f.readlines()
    count = {}
    for line in lines:
        fields = line.split(':')
        if fields[0] == 'Name':
            name=fields[1].split('-')[0].strip()
            if name not in count:
                count[name] = 1
            else:
                count[name] += 1
    for item in sorted(count.items()):
        print(*item, sep=': ')
except:
    print ('File not found')



