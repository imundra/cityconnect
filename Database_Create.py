import sqlite3
conn = sqlite3.connect('events.db')
c = conn.cursor()
c.execute('''CREATE TABLE events
             (Day, Start, End)''')
conn.commit()
conn.close()
