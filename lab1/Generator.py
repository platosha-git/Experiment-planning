from typing import List, Callable
from Request import Request
from random import random
import numpy.random as nr

from Event import Event

class Generator:
    def __init__(self, timeDistribution, next: Callable[[Request], List[Request]]):
        self.reqId = 1
        self.time = 0
        self.timeDistribution = timeDistribution
        self.next = next
        
        self._totalTimePeriod = 0
        self._countPeriods = 0

    def process(self, event: Event = None) -> List[Event]:        
        events: List[Event] = []

        events.append(Request(self.reqId, self.time, self.next, f"запрос {self.reqId:4}"))
        self.reqId += 1
        
        # новое событие генератора
        t = self.timeDistribution()
        self._totalTimePeriod += t
        self._countPeriods += 1
        self.time += t

        events.append(Event(self.time, self.process, "сгенерировать новый запрос"))
        return events

    @property
    def Lambda(self):
        return 1 / (self._totalTimePeriod / self._countPeriods)

# a +- b
def generatorUD(a, b):
    a, b = a - b, a + b
    return lambda: a + (b - a) * random()

def generatorGauss(m, sigma):
    return lambda: nr.normal(m, sigma)

def generatorExponent(t_avg):
    return lambda: nr.exponential(t_avg)