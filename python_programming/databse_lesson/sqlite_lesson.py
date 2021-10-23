import sqlite3

conn = sqlite3.connect('test_sqlite.db')

conn = sqlite3.connect(':memory:')

curs = conn.cursor()

curs.execute(
    'CREATE TABLE person(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
)

curs.execute(
    'INSERT INTO person(name) values("Mike")'
)
curs.execute(
    'INSERT INTO person(name) values("Nancy")'
)

curs.execute(
    'INSERT INTO person(name) values("Jun")'
)
curs.execute('UPDATE person set name = "Michel" WHERE name = "Mike"')
curs.execute('DELETE FROM person WHERE name = "Michel"')
curs.execute('SELECT * FROM person')
print(curs.fetchall())
conn.commit()
curs.close()
conn.close()
