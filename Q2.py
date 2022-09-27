import re

fileName = input("Enter file:")
if len(fileName) < 1:
    file = open('Text.txt')
else:
    file = open(fileName)
d = dict()
for line in file:
    words = line.split()
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
for key in d:
    print(key, "  " , d[key])

