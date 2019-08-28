import abc

from typing import Dict, Any


class Result:
    def __init__(self, data: Dict[str, Any]):
        self._data = data

    @property
    def data(self) -> Dict[str, Any]:
        return self._data

    def format(self, format: str) -> Any:
        pass
