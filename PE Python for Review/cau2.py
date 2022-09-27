name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = {}
for line in handle:
    word = line.split()
    if len(word) < 3 or word[0] != "From" : continue
    full_hour = word[5]
    hour = full_hour.split(":")
    hour = str(hour[:1])
    hour = hour[2:4]
    if hour in counts :
        counts[hour] = 1 + counts[hour]
    else :
        counts.update({hour:1})
lst = list()
for k, v in counts.items():
    new_tup = (k, v)
    lst.append(new_tup)
 
lst = sorted(lst)    
for k, v in lst:
    print(k,v)