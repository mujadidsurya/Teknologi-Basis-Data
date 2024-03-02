import sqlite3

def create_table():
    conn = sqlite3.connect('latihan.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
              (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()
    print('Table berhasil dibuat')
create_table()