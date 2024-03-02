import sqlite3

def get_all_mahasiswa():
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM mahasiswa")
    rows = c.fetchall()
    conn.close()
    return rows

def update_mahasiswa(nim, name, prodi):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("UPDATE mahasiswa SET name = ?, prodi = ? WHERE nim = ?", (name, prodi, nim))
    conn.commit()
    conn.close()

