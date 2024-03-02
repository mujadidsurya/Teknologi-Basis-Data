import sqlite3

def get_all_user():
    conn = sqlite3.connect('sqlite/latihan.sqlite')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return rows

print(get_all_user())