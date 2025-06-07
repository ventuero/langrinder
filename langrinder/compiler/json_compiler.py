import ujson

from langrinder.compiler.abc import ABCCompiler


class JSONCompiler(ABCCompiler):
    @staticmethod
    def compile(source: dict) -> tuple[bool, str | None]:
        if not source:
            return False, None
        return True, ujson.dumps(source, indent=4, ensure_ascii=False)

    @staticmethod
    def load(source: str) -> dict: return ujson.loads(source)
