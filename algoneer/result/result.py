from typing import Any


class Result:
    def __init__(self, data: Any):
        self._data = data

    @property
    def data(self) -> Any:
        return self._data

    def format(self, format: str) -> Any:
        pass
