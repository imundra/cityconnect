import sqlite3

def read():
    conn = sqlite3.connect('events.db')
    c = conn.cursor()
    returned=[]
    timeDict={"6AM":0,"7AM":1,"8AM":2,"9AM":3,"10AM":4,"11AM":5,"12PM":6,"1PM":7,"2PM":8,"3PM":9,"4PM":10,"5PM":11,"6PM":12,"7PM":13,"8PM":14,"9PM":15,"10PM":16,"11PM":17,"12AM":18,"1AM":19,"2AM":20,"3AM":21,"4AM":22,"5AM":23}
    dayDict={"sunday":0,"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6}
    for x in range(24):
        returned.append(["","","","","","",""])
    output=[]
    for row in c.execute('SELECT * FROM events'):
        output+=[list(row)]
    for row in output:
        try:
            dayIndex=dayDict[row[0]]
            startIndex=timeDict[row[1]]
            endIndex=timeDict[row[2]]
            for y in range(startIndex, endIndex):
                returned[y][dayIndex]="XXXXX"
        except:
            continue
    conn.commit()
    conn.close()
    return returned
