from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_system(self) -> AbstractSystem:
        pass


class AbstractSystem(ABC):
    @abstractmethod
    def develop(self) -> str:
        pass

    @abstractmethod
    def production(self) -> str:
        pass


class ConcreteSystemFactory(AbstractFactory):
    def create_system(self) -> AbstractSystem:
        return ConcreteSystem()


class ConcreteSystem(AbstractSystem):
    def develop(self) -> str:
        return 'System: Developing'

    def production(self) -> str:
        return 'System: Production'


def client_code(factory: AbstractFactory) -> None:
    system = factory.create_system()
    print(system.develop())
    print(system.production())


if __name__ == "__main__":
    client_code(ConcreteSystemFactory())
