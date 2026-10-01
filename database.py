import sqlite3

def initialize_database():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            status TEXT NOT NULL,
            date_added TEXT DEFAULT CURRENT_TIMESTAMP,
            date_started TEXT,
            date_finished TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mood_tags (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book_mood_tags (
            book_id INTEGER NOT NULL,
            mood_tag_id INTEGER NOT NULL,
            FOREIGN KEY (book_id) REFERENCES books(id),
            FOREIGN KEY (mood_tag_id) REFERENCES mood_tags(id)
        )    
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS memory_notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER NOT NULL,
            characters TEXT,
            gist TEXT,
            quote TEXT,
            FOREIGN KEY (book_id) REFERENCES books(id)
        )
    ''')

    connection.commit()
    connection.close()

def add_book(title, author, status):
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO books (title, author, status) VALUES (?, ?, ?)', 
            (title, author, status)
        )
        connection.commit()
        connection.close()

def get_all_books():
        connection = sqlite3.connect('books.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        rows = cursor.fetchall()
        connection.close()
        return rows


if __name__ == "__main__":
    initialize_database()
    add_book("The Alchemist", "Paulo Coelho", "TBR")
    print(get_all_books())