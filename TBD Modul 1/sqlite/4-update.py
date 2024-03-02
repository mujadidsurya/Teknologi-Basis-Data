import sqlite3

def get_all_users():
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

def update_user(id, name, age):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    conn.close()

    print("User berhasil diperbarui")

update_user(1, "Jhonny Editer", 32)
print(get_all_users())