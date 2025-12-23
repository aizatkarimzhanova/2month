import sqlite3


def create_table(connection):
    connection.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)
    connection.commit()


def insert_books(connection):
    books = [
    ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 5),
    ("О дивный новый мир", "Олдос Хаксли", 1932, "Антиутопия", 311, 4),
    ("451 градус по Фаренгейту", "Рэй Брэдбери", 1953, "Научная фантастика", 256, 6),
    ("Хоббит", "Дж. Р. Р. Толкин", 1937, "Фэнтези", 310, 7),
    ("Гарри Поттер и философский камень", "Дж. К. Роулинг", 1997, "Фэнтези", 400, 10),
    ("Преступление и наказание", "Фёдор Достоевский", 1866, "Классика", 671, 3),
    ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Философская сказка", 96, 8),
    ("Убить пересмешника", "Харпер Ли", 1960, "Классика", 281, 5),
    ("Скотный двор", "Джордж Оруэлл", 1945, "Политическая сатира", 112, 6),
    ("Алхимик", "Пауло Коэльо", 1988, "Роман", 208, 9)
    ]

    connection.executemany("""
    INSERT INTO books (
        name, author, publication_year, genre,
        number_of_pages, number_of_copies
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    connection.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")

    create_table(conn)
    insert_books(conn)

    conn.close()
