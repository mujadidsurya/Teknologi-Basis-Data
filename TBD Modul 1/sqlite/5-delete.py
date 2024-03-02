import sqlite3

def get_all_users():
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

def delete_user(id):
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()

delete_user(2)
print(get_all_users())