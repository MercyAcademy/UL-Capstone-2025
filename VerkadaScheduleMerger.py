# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:26:30 2025

@author: Perrin
"""

import datetime
import event
import VerkadaCalendar

weights = ['unlocked', 'card_and_code', 'access_controlled', 'locked']

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
    
    
    for door in doorlist:
        currExceptList = currExceptions[door]
        for current in currExceptList:
            currentIndex = currExceptList.index(current)
            previous = currExceptList[currentIndex - 1]
            
            #Begins correction process if the start of the current event is
            #inside of the previous event
            if previous['end_time'] > current['start_time']:
                event0 = weights.index(previous['door_status'])
                event1 = weights.index(current['door_status'])
                #If the current event is wholely within the previous event,
                #Check which has more priority
                if previous['end_time'] > current['end_time']:
                    #If the current event has higher priority, split previous
                    #Event in two
                    if event0 < event1:
                        tempTime = previous['end_time']
                        previous['end_time'] = current['start_time']
                        #new event is end half of previous event
                        newEvent = {'door_status' : current['door_status'], 'start_time' : current['end_time'], 'end_time' : tempTime}
                        currExceptList.insert(currentIndex + 1, newEvent)
                    #If the current event has lower priority, just delete it.
                    else:
                        currExceptList.remove(current)
                #If the only discrepancy is the edges, just shorten the event
                #based on which one has higher priority
                else:
                    if event0 < event1:
                        previous['end_time'] = current['start_time']
                    else:
                        current['start_time'] = previous['end_time']
        allEventList.update({door : currExceptList})
        
    
    return allEventList
        

if __name__ == "__main__":
    schedule = mergeVerkadaSchedule(datetime.datetime.now(), datetime.MAXYEAR)
    