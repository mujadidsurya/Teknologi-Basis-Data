import sqlite3

# CREATE TABLE
def create_table():
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
              (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()
    print('Table berhasil dibuat')
create_table()

# INSERT DATA
def add_user(name, age):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()
    print("User berhasil ditambahkan")
add_user('John', 30)
add_user('Alice', 30)

# READ DATA
def get_all_users():
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows
print(get_all_users())

# UPDATE DATA
def update_user(id, name, age):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    conn.close()

    print("User berhasil diperbarui")
update_user(1, "Jhonny Editer", 32)
print(get_all_users())

# DELETE DATA
def delete_user(id):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
delete_user(2)
print(get_all_users())