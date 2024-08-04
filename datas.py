import sqlite3

def init_db():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY,
                            username TEXT,
                            first_name TEXT,
                            last_name TEXT
                        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            computer_id INTEGER,
                            start_time TEXT,
                            end_time TEXT,
                            FOREIGN KEY(user_id) REFERENCES users(id)
                        )''')
        conn.commit()

def add_user(user_id, username, first_name, last_name):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT OR IGNORE INTO users (id, username, first_name, last_name)
                          VALUES (?, ?, ?, ?)''', (user_id, username, first_name, last_name))
        conn.commit()

def add_reservation(user_id, computer_id, start_time, end_time):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO reservations (user_id, computer_id, start_time, end_time)
                          VALUES (?, ?, ?, ?)''', (user_id, computer_id, start_time, end_time))
        conn.commit()

def get_reservations():
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM reservations''')
        return cursor.fetchall()

def get_computer_reservations(computer_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM reservations WHERE computer_id = ?''', (computer_id,))
        return cursor.fetchall()

def finish_reservation_by_user_id(user_id):
    with sqlite3.connect('database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''DELETE FROM reservations WHERE user_id = ?''', (user_id,))
        conn.commit()
