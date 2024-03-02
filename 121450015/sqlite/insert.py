import sqlite3

def add_mahasiswa(nim, name, prodi):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO mahasiswa (nim, name, age) VALUES (?, ?, ?)", (nim, name, prodi))
    conn.commit()
    conn.close()
