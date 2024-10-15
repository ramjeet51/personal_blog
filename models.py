# models.py
import sqlite3

def connect_db():
    return sqlite3.connect('database.db')

def create_table():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def add_post(title, content, tags):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts (title, content, tags) VALUES (?, ?, ?)', (title, content, tags))
        conn.commit()

def get_posts():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts ORDER BY created_at DESC')
        return cursor.fetchall()

def get_post(post_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts WHERE id = ?', (post_id,))
        return cursor.fetchone()

def update_post(post_id, title, content, tags):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE posts SET title = ?, content = ?, tags = ? WHERE id = ?', (title, content, tags, post_id))
        conn.commit()

def delete_post(post_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM posts WHERE id = ?', (post_id,))
        conn.commit()
