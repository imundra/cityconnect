import sqlite3

def remove(Day):
    Day=Day.lower()
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    c.execute("DELETE FROM events WHERE Day LIKE '%" + str(Day).lower() + "%'")
    conn.commit()
    conn.close()
