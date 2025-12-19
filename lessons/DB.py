
import sqlite3

def crete_tables(connection):
    connection.execute(""" 
    CREATE TABLE IF NOT EXIST students(
        name TEXT,  
        age INTEGER,
        city TEXT
        )
    """)
def add_students(connection, name, age, city):
    connection.execute("""
    INSERT INTO students VALUES("aizat", 20, "bishkek)
""")
    connection.commit()

if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    crete_tables(conn)





    
