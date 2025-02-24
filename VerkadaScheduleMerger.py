import datetime
import VerkadaCalendar

weights = ['unlocked', 'card_and_code', 'access_controlled', 'locked']

def mergeVerkadaSchedule():  
    currExceptions = VerkadaCalendar.retrieveCalendar()
    
    for door in currExceptions:
        previous = None
        newExceptionList = []
        for exception in currExceptions[door]:
            if previous != None and previous['end_time'].date() == exception['start_time'].date() and (previous['end_time'] > exception['start_time']):
                if previous['end_time'] > exception['end_time']:
                    if weights.index(previous['door_status']) < weights.index(exception['door_status']):
                        newEvent = {'door_status' : previous['door_status'], 'start_time' : exception['end_time'], 'end_time' : previous['end_time']}
                        newExceptionList.append(exception)
                        newExceptionList.append(newEvent)
                        newExceptionList[len(newExceptionList) - 1]['end_time'] = exception['start_time']
                        previous = newEvent
                        break

                elif previous['end_time'] < exception['end_time']:
                    if weights.index(previous['door_status']) < weights.index(exception['door_status']):
                        newExceptionList[len(newExceptionList) - 1]['end_time'] = exception['start_time']
                    else:
                        exception['start_time'] = newExceptionList[len(newExceptionList) - 1]['end_time']
            
            newExceptionList.append(exception)
            previous = exception
            
        currExceptions[door] = newExceptionList
        
    return currExceptions

if __name__ == "__main__":
    print(mergeVerkadaSchedule())