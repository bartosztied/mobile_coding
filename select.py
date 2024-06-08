import sqlite3

conn = sqlite3.connect("tutorial.db")
cursor = conn.cursor()

res = cursor.execute("SELECT * FROM movie")
print (res.fetchall())

conn.close()
