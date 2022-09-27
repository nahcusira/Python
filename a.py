import re

hand = open("D:\\FPT\\Semester5\\PRP201c\\regex_sum_1566371.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)