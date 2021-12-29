from abc import ABC, abstractmethod


class ITimer(ABC):

    @abstractmethod
    def start(self) -> None:
        """Start timer for an activity."""

    @abstractmethod
    def end(self) -> None:
        """End timer for an activity"""


class ILogger(ABC):

    @abstractmethod
    def record(self) -> None:
        """This method triggers everytime timer starts and saves it to the
        Database whenever timer is ended."""


class Database:
    pass


class App:
    pass
