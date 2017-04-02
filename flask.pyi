from typing import Callable, Sequence, Dict
from mypy_extensions import NoReturn


class Flask:
    def __init__(self, name: str) -> None: ...
    def route(self, rule: str, methods: Sequence[str]=None) -> Callable: ...
    def run(self, debug: bool=False) -> NoReturn: ...

class _Request:
    form: Dict[str, str]


request = _Request()
