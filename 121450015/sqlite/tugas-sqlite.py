import sqlite3

# Membuat Table
def create_table():
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS mahasiswa 
              (nim INTEGER PRIMARY KEY, name TEXT, prodi TEXT)''')
    conn.commit()
    conn.close()

# Insert Data
def add_mahasiswa(nim, name, prodi):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO mahasiswa (nim, name, prodi) VALUES (?, ?, ?)", (nim, name, prodi))
    conn.commit()
    conn.close()

# Menampilkan Data
def get_all_mahasiswa():
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM mahasiswa")
    rows = c.fetchall()
    conn.close()
    return rows

# Update Data
def update_mahasiswa(nim, name, prodi):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("UPDATE mahasiswa SET name = ?, prodi = ? WHERE nim = ?", (name, prodi, nim))
    conn.commit()
    conn.close()

# Delete Data
def delete_mahasiswa(nim):
    conn = sqlite3.connect('sqlite/mahasiswa.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
    conn.commit()
    conn.close()

#Memanggil Fungsi
create_table()

add_mahasiswa(101, "Arya Wicaksono Pratama", "Program Studi Teknik Industri") 
add_mahasiswa(102, "Sofia Elara", "Program Studi Teknik Pertambangan") 
add_mahasiswa(121450015, "Mujadid Choirus Surya", "Program Studi Sains Data")

print("All Mahasiswa:") 
print(get_all_mahasiswa())

update_mahasiswa(101, "Arya Wicaksono Pratama", "Program Studi Teknik Perkeretaapian") 
update_mahasiswa(121450015, "Mujadid Choirus Surya", "Program Studi Arsitektur Lanskap")
print("After update:")
print(get_all_mahasiswa())

delete_mahasiswa(102)
print("After delete:")
print(get_all_mahasiswa())