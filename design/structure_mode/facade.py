from __future__ import annotations


class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        result = [
            "Facade initializes subsystems:",
            self._subsystem1.operation1(),
            self._subsystem2.operation1(),
            "Facade orders subsystems to perform the action:",
            self._subsystem1.operation_n(),
            self._subsystem2.operation_z()
        ]
        return "\n".join(result)


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Fire!"


def client_code(facade: Facade) -> None:
    print(facade.operation(), '')


if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
