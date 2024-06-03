from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"update success! current : {product.operation()}"

        return result


class System(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Develop(System):
    def operation(self) -> str:
        return 'Develop'


class Production(System):
    def operation(self) -> str:
        return 'Production'


class ConcreteDevelop(Creator):
    def factory_method(self) -> System:
        return Develop()


class ConcreteProduction(Creator):
    def factory_method(self) -> System:
        return Production()


def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    client_code(ConcreteDevelop())
    client_code(ConcreteProduction())
