import re

f = open('file.txt','r')
lines = f.readlines()
regex = re.compile(r'((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}')
for line in lines:
    if regex.match(line):
        print(line)