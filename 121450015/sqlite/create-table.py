import sqlite3

def create_table():
    conn = sqlite3.connect('mahasiswa.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mahasiswa 
              (nim INTEGER PRIMARY KEY, name TEXT, prodi TEXT)''')
    conn.commit()
    conn.close()

