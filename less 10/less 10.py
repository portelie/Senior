import sqlite3

conn = sqlite3.connect('1222_DB.sl3', 5)
cur = conn.cursor()
# CREATE

cur.execute("CREATE TABLE student(id int, name VARCHAR, age INT);")
# ALTER
# DROP

# INSERT
# SELECT