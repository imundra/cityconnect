import sqlite3

def add(Day, Start, End):
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    Day=Day.lower()
    Start=Start.upper()
    End=End.upper()
    stringInput = "("
    listed = [Day, Start, End]
    for x in range(len(listed)):
        if x!=2:
            stringInput = stringInput + "'" + str(listed[x]) + "',"
        else:
            stringInput = stringInput + "'" + str(listed[x]) + "')"
    c.execute("INSERT INTO events VALUES " + stringInput)
    conn.commit()
    conn.close()
