import sqlite3


try:
    f= open('Trace.txt','r')
    conn = sqlite3.connect('Trace.sqlite')
    conn.executescript(
        '''
        drop table if exists Providers;
        CREATE TABLE Providers (Pname TEXT, Pcount INTEGER, Pwarning TEXT );
        '''
    )
    lines = f.readlines()
    count = {}
    for line in lines:
        fields = line.split(':')
        if fields[0] == 'Name':
            name=fields[1].split('-')[0].strip()
            if name not in count:
                count[name] = 1
            else:
                count[name] += 1
    for item in sorted(count.items()):
        if item[1] > 1:
            warning = 'High risk'
        else:
            warning = 'Normal'
        conn.execute('insert into Providers values (?,?,?);', (item[0], item[1], warning))
    conn.commit()
    rows = conn.execute('select * from Providers ORDER BY Pcount DESC')
    print('Troubleshoot wired LAN related issues: ')
    print('Provide'.ljust(15, ' ') + 'Count'.ljust(10, ' ') + 'Warning'.ljust(10, ' '))
    for row in rows:
        print(row[0].ljust(15, ' ') + str(row[1]).ljust(10, ' ') + row[2].ljust(10, ' '))
    conn.commit()
    f.close()
    conn.close()
except Exception as e:
    print(e)