import sqlite3

# dočasná cesta
DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.SQLITE_ERROR:
        print("Nepodařilo se připojit k databázi.")

def create_db():
    conn = connect_db()
    script = "shop.sql"
    with open(script, "r") as file:
        conn.executescript(file.read())
    conn.commit()
    conn.close()

def db_execute(command, params=False, path=DB_PATH):
    conn = connect_db(path)
    if params:
        result = conn.execute(command, params).fetchall()
    else:
        result = conn.execute(command).fetchall()
    conn.commit()
    conn.close()
    return result