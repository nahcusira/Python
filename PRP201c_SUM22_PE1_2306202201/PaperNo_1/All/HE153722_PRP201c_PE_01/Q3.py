import re
import sqlite3
lines = open('Data.txt','r')
con = sqlite3.connect('Mark.sqlite')
con.executescript(
    '''
    drop table if exists Marks;
    create table Marks(
        ID text,
        Name text,
        Math float,
        Physic float,
        Chemis float,
        Sum float,
        Result text
    );
    '''
)
lines = open('Data.txt', 'r')
name = id = result = ''
math = physic = chemis = sum = 0.0
for line in lines:
    fields = re.split('\\s+', line)
    if fields[0] == 'ID':
        continue
    id = fields[0]
    name = fields[1] + ' ' + fields[2] + ' ' + fields[3]
    math = float(fields[4])
    physic = float(fields[5])
    chemis = float(fields[6])
    sum = math + physic + chemis
    if sum >= 15:
        result = 'Pass'
    else:
        result = 'Not Pass'
    con.execute('insert into Marks values (?, ?, ?, ?, ?, ?, ?);', (id, name, math, physic, chemis, sum, result))
con.commit()
table = con.execute('select * from Marks where sum > 10 order by sum desc;')
print('Student list:')
print('ID'.ljust(15,' '),'Full Name'.ljust(15,' '),'Math'.ljust(15,' '),'Physic'.ljust(15,' '),'Chemis'.ljust(15,' '),'Sum'.ljust(15,' '),'Result'.ljust(15,' ') )
for row in table:
    print(str(row[0]).ljust(15,' '), str(row[1]).ljust(15,' '),str(row[2]).ljust(15,' '), str(row[3]).ljust(15,' '), str(row[4]).ljust(15,' '), str(row[5]).ljust(15,' '), str(row[6]).ljust(15,' '))