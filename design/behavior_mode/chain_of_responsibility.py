from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> None:
        pass

    @abstractmethod
    def handler(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handler(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handler(request)

        return super().handler(request)


class MonkeyHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == 'Banana':
            return f"Monkey: I'll eat the {request}"

        return super().handler(request)


class SquirrelHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        return super().handler(request)


class DogHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        return super().handler(request)


def client_code(handler: Handler) -> str:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handler(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
