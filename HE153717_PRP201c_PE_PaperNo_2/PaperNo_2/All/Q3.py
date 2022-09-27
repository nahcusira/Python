import sqlite3
import re

conn = sqlite3.connect('Bills.sqlite')

conn.executescript('''
    DROP TABLE IF EXISTS Bill;
    CREATE TABLE Bill(
        ID text,
        Name text,
        Type text,
        NumOfKw int,
        Price int,
        Money int
    );
''')
price = 0
lines = open('CustomerBills.txt','r')
for line in lines:
    lst = re.split("\\s+",line)
    if lst[0] == 'ID':
        continue

    id1 = lst[0]
    name = lst[1] + ' ' + lst[2] + ' ' + lst[3]
    type1 = lst[4]
    numofkw = int(lst[5])

    if type1 == 'A':
        price = 1500       
    elif type1 == 'B':
        price = 2000       
    else:
        price = 2500

    total = price * int(numofkw)
    conn.execute('''
        INSERT INTO Bill(ID,Name,Type,NumOfKw,Price,Money)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (id1,name,type1,numofkw,price,total)
    )
conn.commit()

print('Customer bill list:')
print('ID'.ljust(10,' '),'Full Name'.ljust(15,' '),'Type'.ljust(10,' '),'NumOfKw'.ljust(10,' '),'Price'.ljust(10,' '),'Money'.ljust(10,' '))
table = conn.execute('''select * from bill where money > 150000 order by money asc''')

for row in table:
     print(str(row[0]).ljust(10,' '),str(row[1]).ljust(15,' '),str(row[2]).ljust(10,' '),
           str(row[3]).ljust(10,' '),str(row[4]).ljust(10,' '),str(row[5]).ljust(10,' '),)
