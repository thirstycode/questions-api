import sqlite3
from config import problems_db

conn = sqlite3.connect(problems_db)

c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE stocks(date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("SELECT * FROM stocks")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
print("done")