from abc import ABC, abstractmethod
class Handler:
    @abstractmethod
    def set_next(self):
        pass
    
    @abstractmethod
    def handle(self):
        pass

class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler: Handler):
        self._next_handler = handler
        return self._next_handler
    
    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey Handler: I will eat {request}"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == "Peanut":
            return f"Squirrel Handler: I will eat {request}"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == "MeatBall":
            return f"Dog Handler: I will eat {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler):
    for food in ["Peanut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"{result}", end ="")
        else:
            print(f"  {food} was left untouched.", end="")

if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
    