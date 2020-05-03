import sqlite3

DB_PATH = '/Users/vishalnalwa/projects/project_python/db'
DB_NAME = 'music.sqlite'
conn = sqlite3.connect(DB_PATH+'/'+DB_NAME)
cur = conn.cursor()

cur.execute('INSERT INTO Tracks (title,plays) VALUES(?,?)',('Thudnerstruck', 20))
cur.execute('INSERT INTO Tracks (title,plays) VALUES(?,?)',('My Way', 15))

conn.commit()

print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
print(cur)
for row in cur:
    print(row)

cur.execute('DELETE FROM Tracks WHERE plays < 100')
conn.commit()

cur.close()

