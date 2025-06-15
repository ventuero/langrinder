from abc import ABC, abstractmethod


class ABCCompiler(ABC):
    """Abstract compiler class for Langrinder"""

    @staticmethod
    @abstractmethod
    def compile(source: dict) -> tuple[bool, str | None]: ...

    @staticmethod
    @abstractmethod
    def load(source: str) -> dict: ...
