import sqlite3

conn=sqlite3.connect("tutorial.db")

cursor=conn.cursor()

cursor.execute("CREATE TABLE movie(title,year,score)")

cursor.execute("""
	INSERT INTO movie VALUES
		('Monty Python and the Holy Grail', 1975, 8.2),
        	('And Now for Something Completely Different', 1971, 7.5)
""")

conn.commit()
conn.close()
