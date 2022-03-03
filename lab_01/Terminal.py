from multiprocessing import Event
from Request import Request
class Terminal:
    """Завершающий этап обработки запроса"""
    def __init__(self) -> None:
        # успешно обработаны
        self.processed = 0
        # отклонены
        self.rejected = 0
        self.lastRequest = Request(-1, 0, next=lambda x: [])

    def process(self, request: Request) -> None:
        # print(f"terminal request\t\t\t{request.reqId:4}, {request.time:.2f} min")
        self.lastRequest = request
        self.processed += 1
        return None

    def reject(self, request: Request) -> None:
        # print(f"terminal rejected request\t{request.reqId:4}, {request.time:.2f} min")
        self.lastRequest = request
        self.rejected += 1
        return None

    @property
    def totalProcessed(self):
        return self.rejected + self.processed