import sqlite3
from datetime import datetime

def mark_attendance(name):
    conn = sqlite3.connect('database/attendance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (name, time) VALUES (?, ?)", (name, datetime.now()))
    conn.commit()
    conn.close()
