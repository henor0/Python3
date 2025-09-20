import sqlite3
from tkinter.tix import INTEGER
connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
Create TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salery REAL
)'''
)
connection.commit()

cursor.commit(
    '''
    INSERT INTO employees (name, position, department, salery)
values(?,?,?,?)
''',('John', 'Softwere Enginieer', 'IT', 70000.00)
)
connection.commit()

cursor.execute('SELECT * FROM employess')

rows = cursor.fetchall()

for row in rows:
    print(row)


crusor.execute('''
    UPDATE employess SET salery = ?
    WHERE name = ?
''',(80000.00, 'John')
)

connection.commit()

cursor.execute('''
''', (1,))
connection.commit()
cursor.close()
connection.close()     