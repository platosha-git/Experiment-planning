from __future__ import annotations
from Event import *
from typing import Callable, List

class Request(Event):
    def __init__(self, reqId, initTime: float, next: Callable[[Request], List[Event]], name: str = None) -> None:
        if not name:
            name = f"request №{reqId}"
        Event.__init__(self, initTime, next, name)
        self.reqId = reqId

    # def __str__(self) -> str:
    #     return self.name.ljust(46) + f"{self.time:.2f} min"