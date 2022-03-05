from __future__ import annotations
from typing import Callable, List

class Event:
    def __init__(self, time: float, next: Callable[[Event], List[Event]], name: str = "event") -> None:
        self.time = time
        self.initTime = time
        self.name: str = name
        self.next = lambda: next(self)

    def __str__(self) -> str:
        return self.name.ljust(46) + f"{self.time:.2f} min"