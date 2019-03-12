import sqlite3
from config import problems_db

lang = input("Enter language name: ")

conn = sqlite3.connect(problems_db)

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS %s(difficulty text, question text, choice1 text, choice2 text, choice3 text, choice4 text, ans text, category text)'''%(lang))

# Save (commit) the changes
conn.commit()
conn.close()