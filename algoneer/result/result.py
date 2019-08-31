from typing import Any

import abc


class Result(abc.ABC):
    def __init__(self, data: Any):
        self._data = data

    @abc.abstractproperty
    def name(self) -> str:
        pass

    @abc.abstractproperty
    def version(self) -> str:
        pass

    @property
    def data(self) -> Any:
        return self._data

    def format(self, format: str) -> Any:
        pass
