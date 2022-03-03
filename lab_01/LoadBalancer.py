import queue
from typing import List, Callable
from Request import Request
from Terminal import Terminal
from random import choice

class LoadBalancer:
    def __init__(self, name, consumers: list, terminal: Terminal, capacity = -1) -> None:
        self.name = name
        self.consumers = consumers
        self.terminal = terminal
        self.queue: List[Request] = []
        self.capacity = capacity
        self.maxQueue = 0
        self.processedRequest = 0
        self.processingRequest = 0
        for consumer in consumers:
            consumer.loadBalancer = self

        self.totalWaitingTime = 0

    def process(self, request: Request) -> List[Request]:
        # print(f"load balancer {self.name} request\t\t{request.reqId:4}, {request.time:.2f} min")

        # очередь переполнена
        queueSize = len(self.queue)
        if queueSize == self.capacity:
            # print(f"load balancer {self.name} reject request\t{request.reqId:4}, {request.time:.2f} min")
            return self.terminal.reject(request)

        if self.maxQueue <= queueSize:
            self.maxQueue = queueSize + 1

        # выбор произвольного свободного потребителя
        freeConsumers = [consumer for consumer in self.consumers if not consumer.busy]
        if freeConsumers:
            self.processingRequest += 1
            return choice(freeConsumers).process(request)
        
        # добавление в очередь необработанных заявок
        self.queue.append(request)
        return None

    def free(self, consumer, request: Request) -> List[Request]:
        # потребитель освободился
        # print(f"load balancer {self.name} free request\t{request.reqId:4}, {request.time:.2f} min")
        self.processedRequest += 1

        if len(self.queue) == 0:
            self.processingRequest -= 1
            return None

        req = self.queue.pop(0)
        self.totalWaitingTime += request.time - req.time
        #print(request.time - req.time, request.time, req.time)
        req.time = request.time

        return consumer.process(req)