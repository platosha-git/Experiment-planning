from Terminal import *
from typing import List

from Event import Event

class EventModel:
    def __init__(self, terminal: Terminal) -> None:
        self.events: List[Event] = []
        self.terminal = terminal

    def addEvent(self, event: Event):
        if not event:
            return
        i = 0
        while i < len(self.events) and self.events[i].time <= event.time:
            i += 1
        self.events.insert(i, event) 

    def addEvents(self, events: List[Event]):
        if not events:
            return
        for newEvent in events:
            self.addEvent(newEvent)
    
    # n = -1 неограничивать по числу заявок
    # maxTimeModulation - максимальное время модуляции 
    def run(self, n: int = -1, maxTimeModulation: int = -1):
        while len(self.events) != 0 and self.terminal.totalProcessed != n:
            event = self.events.pop(0)
            # print(event)

            if maxTimeModulation == -1 or event.time < maxTimeModulation:
                self.addEvents(event.next())
            else:
                #print(f"{event.name}, {event.time:.2f} min >= {maxTimeModulation:.2f} min")
                return