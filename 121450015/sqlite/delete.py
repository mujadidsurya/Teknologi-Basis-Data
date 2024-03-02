import sqlite3

def get_all_mahasiswa():
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM mahasiswa")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_mahasiswa(nim):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
    conn.commit()
    conn.close()
