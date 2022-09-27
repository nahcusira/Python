import sqlite3
import re
lines = open("CustomerBills.txt","r")
connect = sqlite3.connect("Bills.sqlite")
connect.executescript(
    '''
    drop table if exists Bill;
    create table Bill(
        ID text not null,
        Name text not null,
        Type text not null,
        NumOfKw integer,
        Price integer,
        Money integer
        );
    '''
)
ID = ""
Name = ""
Type = ""
NumOfKw = 0
Price = 0
Money = 0
for line in lines:
    field = re.split("\\s+",line)
    if(field[0] == "ID"):
        continue
    ID = field[0]
    Name = field[1] +" "+field[2] + " "+field[3]
    Type = field[4]
    NumOfKw = int(field[5])
    if Type == "A":
        Price = 1500
    elif Type == "B":
        Price = 2000
    else:
        Price = 2500
    Money = int(NumOfKw * Price)
    connect.execute('insert into Bill values (?,?,?,?,?,?);',(ID,Name,Type,NumOfKw,Price,Money));
connect.commit()
data = connect.execute('select * from Bill where Money > 150000 order by Money asc;')
print("Customer bill list:")
print("ID".ljust(10,' '),"Full Name".ljust(15,' '),"Type".ljust(10,' '),"NumOfKw".ljust(10,' '),"Price".ljust(10,' '),"Money".ljust(10,' '))
for line in data:
    print(str(line[0]).ljust(10,' '),str(line[1]).ljust(15,' '),str(line[2]).ljust(10,' '),str(line[3]).ljust(10,' '),str(line[4]).ljust(10,' '),str(line[5]).ljust(10,' '))
