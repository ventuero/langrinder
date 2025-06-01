from abc import ABC, abstractmethod

from langrinder.parser import LangrinderBaseParser


class LangrinderBaseGenerator(ABC):
    parser: LangrinderBaseParser

    @classmethod
    @abstractmethod
    def generate(cls, output_file: str, input_dir: str):
        """
        Main generate method.
        Returns None, writes the generated result to output file
        """
        ...
