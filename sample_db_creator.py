import sqlite3

def create_loc_db(name):
    # Establish a connection to the SQLite database
    connection = sqlite3.connect(name)
    curso = connection.cursor()

    # Create the "location" table if it doesn't exist
    create_table = "CREATE TABLE IF NOT EXISTS location (id INTEGER PRIMARY KEY, loc_x real, loc_y real, speed INTEGER)"
    curso.execute(create_table)

    # Create the "violations" table if it doesn't exist
    create_table = "CREATE TABLE IF NOT EXISTS violations (id INTEGER PRIMARY KEY, name text, lic INTEGER, timestamp text, loc_x real, loc_y real)"
    curso.execute(create_table)

    # Commit the transaction and close the database connection
    connection.commit()
    connection.close()


# Call the create_loc_db function to create the "sample.db" database
create_loc_db("sample.db")
