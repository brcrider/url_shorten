# File for managing database
import sqlite3
from contextlib import closing

DB_PATH = 'db.db'

def _get_conn():
    # create a connection with check_same_thread default True; we open/close per call
    return sqlite3.connect(DB_PATH)

# create table if not exists
def create_table():
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS urls(id INTEGER PRIMARY KEY, shortCode TEXT, url TEXT, created_at TIMESTAMP, updated_at TIMESTAMP)')
        conn.commit()

# insert url mapping
def insert_url(shortCode, url, created_at, updated_at):
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO urls (shortCode, url, created_at, updated_at) VALUES (?, ?, ?, ?)', (shortCode, url, created_at, updated_at))
        conn.commit()
        

# get url url by shortCode
def  get_url_url(shortCode):
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM urls WHERE shortCode = ?', (shortCode,))
        row = c.fetchall()
        return row[0] if row else None

# get shortCode url by url
def get_shortCode_url(url_url):
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('SELECT shortCode FROM urls WHERE url = ?', (url_url,))
        row = c.fetchone()
        return row[0] if row else None

# verify if shortCode url exists
def verify_shortCode_url(shortCode):
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('SELECT 1 FROM urls WHERE shortCode = ?', (shortCode,))
        return c.fetchone() is not None

# update url url for a given shortCode url
def update_url(shortCode, new_url, updated_at):
    res = ""
    with closing(_get_conn()) as conn:
        c = conn.cursor()
        c.execute('UPDATE urls SET url = ?, updated_at = ? WHERE shortCode = ?', (new_url, updated_at, shortCode))        
                
        return get_url_url(shortCode)
        
