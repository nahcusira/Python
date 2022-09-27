import sqlite3
import re
lines = open('Data.txt', 'r')
connect = sqlite3.connect('Mark.sqlite')
connect.executescript(
    '''
    drop table if exists Marks;
    create table Marks(
        ID text not null,
        Name text not null,
        Math float,
        Physic float,
        Chemis float,
        Sum float,
        Result text not null
    );
    '''
)
ID = ""
Name = ""
Math = 0.0
Physic = 0.0
Chemis = 0.0
Sum = 0.0
Result = ""
for line in lines:
    field = re.split('\\s+', line)
    if field[0] == 'ID':
        continue;
    ID = field[0]
    Name = field[1] + ' ' + field[2] + ' ' + field[3]
    Math = float(field[4])
    Physic = float(field[5])
    Chemis = float(field[6])
    Sum = float(Math + Physic + Chemis)
    if Sum >= 15:
        Result = "Pass"
    else:
        Result = "Not Pass"
    connect.execute('insert into Marks values(?, ?, ?, ?, ?, ?, ? );', (ID, Name, Math, Physic, Chemis, Sum, Result))
connect.commit()
table = connect.execute('select * from Marks where Sum > 10 order by Sum desc ;')
print('Student list:')
print('ID'.ljust(5,' '), 'Full Name'.ljust(15, ' '), 'Math'.ljust(4, ' '), 'Physic'.ljust(4, ' '), 'Chemis'.ljust(9, ' '), 'Sum'.ljust(5, ' '), 'Result'.ljust(7, ' '))
for row in table:
    print(str(row[0]).ljust(5,' '), str(row[1]).ljust(15, ' '), str(row[2]).ljust(5, ' '), str(row[3]).ljust(5, ' '), str(row[4]).ljust(9, ' '), str(row[5]).ljust(5, ' '), str(row[6]).ljust(7, ' '))