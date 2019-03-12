import sqlite3
from config import problems_db

lang = input("Enter language name : ")
question = input("Enter question : ")
choice1 = input("choice1 : ")
choice2 = input("choice2 : ")
choice3 = input("choice3 : ")
choice4 = input("choice4 : ")
ans = input("correct choice (in number 1-4) : ")
diff = input("enter difficulty level (easy, medium, hard): ")


conn = sqlite3.connect(problems_db)

c = conn.cursor()

# Create table
statement = "INSERT INTO %s VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(lang,diff,question,choice1,choice2,choice3,choice4,ans,diff)
# print(statement)
c.execute(statement)

# Save (commit) the changes
conn.commit()
conn.close()