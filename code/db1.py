import sqlite3

DB_PATH = '/Users/vishalnalwa/projects/project_python/db'
DB_NAME = 'music.sqlite'
conn = sqlite3.connect(DB_PATH+'/'+DB_NAME)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT , plays INTEGER)')

conn.close()
