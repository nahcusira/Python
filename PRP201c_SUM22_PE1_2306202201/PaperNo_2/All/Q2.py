import re
fname = input("Enter file:")
if len(fname) < 1:
    fname = "Text.txt"
lines = open(fname, "r")

d = dict()
for line in lines:
    line = line.strip()
    field = re.split("\\s+",line)
    for word in field:
        word = word.strip(".")
        d[word] = d.get(word, 0) + 1

for key in d:
    print(key,":", d[key])


