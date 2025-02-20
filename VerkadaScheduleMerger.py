# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:26:30 2025

@author: Perrin
"""

import datetime
import event
import VerkadaCalendar

#If this needs to be used for other stuff, we can move this to the event class if need be
def statusToWeight(status):
    #Unlocked weighted 4 because it has highest priority, checked first because
    #it's most common
    if (status == 'unlocked'):
        return 1
    #Unlocked weighted 2 because it has second lowest priority, checked second because
    #it's second most common
    if (status == 'access_controlled'):
        return 3
    #Unlocked weighted 3 because it has second highest priority, checked third because
    #it's second least common
    if (status == 'card_and_code'):
        return 2
    #Unlocked weighted 1 because it has lowest priority, checked last because
    #it's least common
    if (status == 'locked'):
        return 4
    #If the program has no idea what it's reading, this is what it'll spit out.
    return -1

def mergeVerkadaSchedule(startDay, endDay):
    #TODO! Replace this when Verkada implements schedule API access
    
    
    currExceptions = VerkadaCalendar.retrieveCalendar()
    doorlist = []
    exceptionArr = []
    #Probably should be optimized once completed.
    #Gets the list of doors from exceptions dict
    for i in currExceptions:
        #print(i)
        doorlist.append(i)
    
    #gets every exception from the exceptions dict using door list
    for i in doorlist:
        currList = currExceptions[i]
        exceptionArr.append(currList)
    
    allEventList = {}
    
    #Runs through dict provided by Verkada API and transforms it into events.
    for i in range(len(doorlist)):
        eventList = []
        for j in exceptionArr[i]:
            #print(j)
            tempEvent = event.Event(j['start_time'], j['end_time'], doorlist[i], j['door_status'])
            eventList.append(tempEvent)
        allEventList.update({doorlist[i] : eventList})
    
    #There's probably a way to do this that doesn't involve going through the
    #list twice, but this way seems easier in regards to keeping everything
    #ordered properly.
    for i in range(len(doorlist)):
        currDoor = doorlist[i]
        for j in range(1, len(allEventList[currDoor])):
            
            #For loop does not update len after deletion, this is just to make
            #sure it actually stops when it is supposed to
            if j >= len(allEventList[currDoor]):
                break
            
            
            #print(j)
            #print(allEventList[currDoor][j-1].startTime, allEventList[currDoor][j-1].endTime)
            #print(allEventList[currDoor][j])
            #If the start time of the current event is before the end time of
            #the previous event, begin correction
            if allEventList[doorlist[i]][j-1].endTime > allEventList[doorlist[i]][j].startTime:
                event0 = statusToWeight(allEventList[doorlist[i]][j-1].eventType)
                event1 = statusToWeight(allEventList[doorlist[i]][j].eventType)
                #If the current event is wholely within the previous event,
                #Check which has more priority
                if allEventList[doorlist[i]][j-1].endTime > allEventList[doorlist[i]][j].endTime:
                    #If the current event has higher priority, split previous
                    #Event in two
                    if event0 < event1:
                        tempTime = allEventList[doorlist[i]][j-1].endTime
                        allEventList[doorlist[i]][j-1].endTime = allEventList[doorlist[i]][j].startTime
                        newEvent = event.Event(allEventList[doorlist[i]][j].endTime, tempTime, doorlist[i], allEventList[doorlist[i]][j-1].eventType)
                        allEventList[doorlist[i]].insert(j+1, newEvent)
                    #If the current event has lower priority, just delete it.
                    else:
                        allEventList[doorlist[i]].remove(allEventList[doorlist[i]][j])
                        j = j - 1
                #If the only discrepancy is the edges, just shorten the event
                #based on which one has higher priority
                else:
                    if event0 < event1:
                        allEventList[doorlist[i]][j-1].endTime = allEventList[doorlist[i]][j].startTime
                    else:
                        allEventList[doorlist[i]][j].startTime = allEventList[doorlist[i]][j-1].endTime
        print(currDoor)
        for j in allEventList[doorlist[i]]:
            print(j.startTime, j.endTime, j.eventType)
        input()
    
    return allEventList
        

if __name__ == "__main__":
    schedule = mergeVerkadaSchedule(datetime.datetime.now(), datetime.MAXYEAR)
    