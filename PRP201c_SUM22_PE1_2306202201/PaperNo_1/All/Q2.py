def getLines():
    while True:
        try:
            filename = input('Enter file:')
            if not filename:
                filename = 'Text.txt'
            lines = open(filename, 'r')
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')
dic = {}
lines = getLines()
count = 0
for line in lines:
    count+=1
    if(count == 1):
        line = line[0:(len(line)-3)]
        words = line.split(", ")
        for word in words:
            dic[word] = dic.get(word, 0) + 1
    else:
        words = line.split(", ")
        for word in words:
            word = word.strip()
            dic[word] = dic.get(word, 0) + 1

print("The converted dictionary is:")
for key in dic:
    print(key.replace(":",""))