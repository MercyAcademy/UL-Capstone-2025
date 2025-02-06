# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:54:36 2025

@author: Perrin
"""

class Event:
    def __init__(self, start, end, doors, code):
        self.startTime = start
        self.endTime = end
        self.eventDoors = doors
        self.eventType = code