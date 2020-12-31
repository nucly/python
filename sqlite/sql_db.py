import sqlite3

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books
            (title TEXT, pages INTEGER)''')

c.execute('INSERT INTO books VALUES ("Are You My Mother?", 72)')
conn.commit()

books = [
    ("Are you my mother", 72),
    ("Harry Poter", 300),
    ("Game of Thrones", 400)
]

c.executemany('INSERT INTO books VALUES (?, ?)', books)
conn.commit()

c.execute('SELECT * FROM books WHERE title="Harry Poter"')
data = c.fetchall()
print(data)

c.execute('UPDATE books SET title="New Book" WHERE rowid=2')

c.execute('DELETE FROM books WHERE rowid=1')
conn.commit()



c.execute('SELECT * FROM books')
data = c.fetchall()
conn.commit()
print(data)