# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:56:08 2025

@author: Perrin
"""
import datetime


if __name__ == "__main__":
    import event
    start = datetime.datetime(2020, 5, 17, 12, 30, 00)
    end = datetime.datetime(2020, 5, 17, 13, 45, 1)
    
    thisEvent = event.Event(start, end, [4,5,6], "Locked")
    
    print(thisEvent.eventType)
    print(thisEvent.startTime)
    print(thisEvent.endTime)