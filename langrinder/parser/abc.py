from abc import ABC, abstractmethod


class ABCParser(ABC):
    @abstractmethod
    def parse_all(self) -> None | dict[str, str]: ...
