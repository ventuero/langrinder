from abc import ABC, abstractmethod
from typing import Any


class ABCCompiler(ABC):
    @staticmethod
    @abstractmethod
    def compile(source: dict) -> tuple[bool, Any | None]: ...

    @staticmethod
    @abstractmethod
    def load(source: Any) -> dict | None: ...
