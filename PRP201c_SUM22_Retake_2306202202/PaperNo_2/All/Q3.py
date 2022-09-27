import re
import sqlite3

def getLines():
    while True:
        try:
            filename = input('Enter file: ')
            if not filename:
                filename = 'Student.txt'
            inFile = open(filename, 'r')
            lines = inFile.readlines()
            inFile.close()
            return lines
        except (FileNotFoundError, IOError):
            print('File not found or unreadable.')


lines = getLines()
conn = sqlite3.connect('Student.sqlite')
conn.executescript(
    '''
    drop table if exists Student;
    create table Student (
        Name TEXT not null,
        Course TEXT not null,
        Grade INTEGER not null,
        Description TEXT not null
    );
    '''
)

for line in lines:
    des = ''
    fields = re.split(r'\s+', line)
    if fields[0] == 'Class':
        continue
    if int(fields[2]) >= 50:
        des = 'Pass'
    else:
        des = 'Fail'
    conn.execute('insert into Student values (?, ?, ?, ?);', (fields[1], fields[0], int(fields[2]), des))
conn.commit()
tables = conn.execute('select * from Student order by Grade desc;')
print('Student list:')
print('Name'.ljust(15,' '), 'Course'.ljust(15,' '), 'Grade'.ljust(15,' '), 'Description'.ljust(15,' '))
for row in tables:
    if (row[2] >= 80):
        print(row[0].ljust(15,' '), row[1].ljust(15,' '), str(row[2]).ljust(15,' '), row[3].ljust(15,' '))