from abc import ABC, abstractmethod
class Handler(ABC):
    def __init__(self, next=None):
        self._next_handler = next

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandlerA(Handler):
    def handle(self, request):
        if request < 10:
            print(f"Request {request} is handled by handler A")
        else:
            self._next_handler.handle(request)

class ConcreteHandlerB(Handler):
    def handle(self, request):
        if request >= 10 and request <= 20:
            print(f"Request {request} is handled by handler B")
        else:
            self._next_handler.handle(request)

class ConcreteHandlerC(Handler):
    def handle(self, request):
        if request > 20:
            print(f"Request {request} is handled by handler C")
        else:
            self._next_handler.handle(request)

if __name__ == "__main__":
    handler_A = ConcreteHandlerA(ConcreteHandlerB(ConcreteHandlerC()))
    # handler_B = ConcreteHandlerB(handler_A)
    # handler_C = ConcreteHandlerC(handler_B)

    for req in [5,15,25]:
        handler_A.handle(req)