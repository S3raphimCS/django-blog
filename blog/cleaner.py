import sqlite3
import os

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
counter = 0

for el in list(os.walk('uploads'))[0][2]:
    cur.execute(f'SELECT * FROM articles_article WHERE picture="uploads/{el}"')
    if not cur.fetchall():
        os.remove(f'uploads/{el}')
        counter += 1

con.close()
print(f'Was deleted {counter} items')