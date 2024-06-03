from __future__ import annotations
from abc import ABC, abstractmethod


class Setting:
    def __init__(self) -> None:
        self.dev = None
        self.test = None

    def set_dev(self, dev: str) -> None:
        self.dev = dev

    def set_test(self, test: str) -> None:
        self.test = test


class Builder(ABC):
    @property
    @abstractmethod
    def settings(self) -> Setting:
        pass

    @abstractmethod
    def set_settings(self, settings: Setting) -> None:
        pass

    @abstractmethod
    def set_test(self, test: str) -> None:
        pass

    @abstractmethod
    def set_dev(self, dev: str) -> None:
        pass


class SettingBuilder(Builder, ABC):
    def __init__(self):
        self._setting = None
        self.reset()

    def reset(self) -> None:
        self._setting = Setting()

    @property
    def settings(self) -> Setting:
        settings = self._setting
        self.reset()
        return settings

    def set_settings(self, setting: Setting) -> None:
        self._setting = setting

    def set_test(self, test: str) -> None:
        self._setting.test = test

    def set_dev(self, dev: str) -> None:
        self._setting.dev = dev


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, build: Builder) -> None:
        self._builder = build

    def build_setting(self, settings: Setting) -> None:
        self.builder.set_settings(settings)

    def build_test(self, test: str) -> None:
        self.builder.set_test(test)

    def build_dev(self, dev: str) -> None:
        self.builder.set_dev(dev)


if __name__ == "__main__":
    director = Director()
    builder = SettingBuilder()
    director.builder = builder

    setting = Setting()
    setting.set_dev('setting_dev')
    setting.set_test('setting_test')

    # Test Case 1
    print("Test Case 1:")
    director.build_setting(setting)
    result_setting = builder.settings
    print(f"Dev Environment: {result_setting.dev}")
    print(f"Test Environment: {result_setting.test}")
    print()

    # Test Case 2
    print("Test Case 2:")
    director.build_dev('dev_from_director')
    director.build_test('test_from_director')
    result_setting = builder.settings
    print(f"Dev Environment: {result_setting.dev}")
    print(f"Test Environment: {result_setting.test}")
