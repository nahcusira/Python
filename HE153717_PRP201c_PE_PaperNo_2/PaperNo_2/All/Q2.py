try:
    fname = input("Enter file: ")
    if len(fname) < 1 :
        lines = open("Text.txt", 'r')
    else:
        lines = open(fname , 'r')
    word = dict()

    for line in lines:
        lst = line.rstrip().split()
        for lst1 in lst:
            word[lst1] = word.get(lst1, 0) + 1

    for k, v in word.items():
        print(k, ':', v)
        
    lines.close()
except (FileNotFoundError, IOError):
    print('File not found')