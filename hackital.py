import requests
def hoursOfOperation(string):
    dictionary={'Sunday':'','Monday':'','Tuesday':'','Wednesday':'','Thursday':'','Friday':'','Saturday':''}
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    times = ["6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM", "10 PM", "11 PM"]

    initialIndex = string.find("Open today")
    string = string[initialIndex:]
    
    index = string.index("_Map")
    relevantTimeSubString = string[index:]
    
    for day in days:
        index = relevantTimeSubString.index(day)
        timeString = relevantTimeSubString[index+len(day):index+70]
        
        startTime = ""
        endTime = ""
    
        startDone = False
        startStarted = False
        endStarted = False
    
        for i in timeString:
            if(i in "1234567890:AMP" and startDone == False):
                startTime += i
                startStarted = True
            elif(startDone == True and startStarted == True):
                if(i in "1234567890:PMA"):
                    endTime += i
                    endStarted = True
                elif(endStarted == True):
                    break
            elif(startStarted == True):
                startDone = True
        if(startTime != "24" and endTime != "24"):
            if("AM" not in startTime and "PM" not in startTime):
                if("AM" in endTime):
                    startTime += "AM"
                else:
                    startTime += "PM"
            if("AM" not in endTime and "PM" not in endTime):
                if("AM" in startTime):
                    endTime += "AM"
                else:
                    endTime += "PM"
            miniList=[]
            miniList.append(startTime)
            miniList.append(endTime)
            dictionary[day] = miniList
        else:
            startTime = "Open 24 hours"
            endTime=""

    return string, dictionary

def stayDuration(string):
    index = string.find("People typically spend")
    string = string[index:]

    index = string.index("<b>")
    index2 = string.index("</b>")
    spendTime = string[index+3:index2]

    index = string.find("is_inferred_hours")
    string = string[index:]
    return string, spendTime

def query(q):
    #q = raw_input("Enter place name: ")
    dictionary = {"q" : q,
              "oq" : q,
              "aqs": "chrome.0.69i59.2480j0j9",
                  "sourceid" : "chrome",
                  "ie" : "UTF-8"}
    
    #Query the place entered
    r = requests.get("https://www.google.com/search", params=dictionary, headers=ua)
    page = str(r.content)
    string = page

    #Get hours of operation of place
    
    miniList=[]
    spendTime=0
    try:
        string,miniList = hoursOfOperation(string)
    except:
        print("Hours of operation are unavailable.")
    #Get the time that people typically spend here
    try:
        string,spendTime = stayDuration(string)
        #print("People typically spend " + spendTime)

    except:
        print("Typical time spent here is unavailable.")
        
    return miniList,spendTime
    
global ua
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
#miniList,spendTime=hackital.query(places[val][0]+" " +places[val][3])
