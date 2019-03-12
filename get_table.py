import sqlite3
from config import problems_db

lang = input("Enter language name: ")

conn = sqlite3.connect(problems_db)

c = conn.cursor()

# Create table
c.execute('''SELECT * FROM %s'''%(lang))

rows = c.fetchall()
for row in rows:
	print(row)

# Save (commit) the changes
conn.commit()
conn.close()