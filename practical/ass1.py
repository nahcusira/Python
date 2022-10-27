import re


a = input()
s = re.split("\\s+", a)
last = s[-1]
print(len(last))