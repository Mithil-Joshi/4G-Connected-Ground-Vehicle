import sqlite3

def create_loc_db(name):
    connection = sqlite3.connect(name)
    curso = connection.cursor()

    create_table = "CREATE TABLE IF NOT EXISTS location (id INTEGER PRIMARY KEY, loc_x real, loc_y real, speed INTEGER)"
    curso.execute(create_table)

    create_table = "CREATE TABLE IF NOT EXISTS violations (id INTEGER PRIMARY KEY, name text, lic INTEGER, timestamp text, loc_x real, loc_y real)"
    curso.execute(create_table)

    connection.commit()
    connection.close()


create_loc_db("sample.db")