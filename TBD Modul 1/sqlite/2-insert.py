import sqlite3

def add_user(name, age):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print("User berhasil ditambahkan")

add_user('John', 30)
add_user('Alice', 30)