from typing import List, Callable
from Request import Request
from Event import Event
from random import random
from LoadBalancer import LoadBalancer

class Device:
    def __init__(self, name, timeDistribution, next: Callable[[Request], List[Event]]) -> None:
        self.name = name
        self.busy = False
        self.timeDistribution = timeDistribution
        self.next = next
        self.loadBalancer: LoadBalancer = None

        self._totalTimePeriod = 0
        self._countPeriods = 0

    def process(self, request: Request) -> List[Request]:
        if self.busy:
            raise Exception(f"Apparatus {self.name} reject request\t\t{request.reqId:4}, {request.time:.2f} min")
        
        def requestNext():
            # print(f"Apparatus {self.name} free request\t\t{request.reqId:4}, {request.time:.2f} min")

            self.busy = False
            if self.loadBalancer:
                req = self.loadBalancer.free(self, request)
                requests = self.next(request)
                if not requests:
                    return req
                if not req:
                    return requests
                req.extend(requests)
                return req
            return self.next(request)

        request.next = requestNext

        # print(f"Apparatus {self.name} busy request\t\t{request.reqId:4}, {request.time:.2f} min")
        self.busy = True

        t = self.timeDistribution()
        self._totalTimePeriod += t
        self._countPeriods += 1
        request.time += t

        return [request]

    @property
    def Mu(self):
        return 1 / (self._totalTimePeriod / self._countPeriods)
