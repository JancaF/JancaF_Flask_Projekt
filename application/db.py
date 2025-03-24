import sqlite3

from flask import current_app, app

# dočasná cesta
DB_PATH = "database.sqlite"

def connect_db(db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.SQLITE_ERROR:
        print("Nepodařilo se připojit k databázi.")

def create_db():
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:
        with open(current_app.config["DB_SCHEME"]) as scheme:
            conn.executescript(scheme.read())
    conn.commit()

def db_execute(command, params=False, path=DB_PATH):
    with sqlite3.connect(current_app.config["DATABASE"]) as conn:
        if params:
            result = conn.execute(command, params).fetchall()
        else:
            result = conn.execute(command).fetchall()
    conn.commit()
    return result

