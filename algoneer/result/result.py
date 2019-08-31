from typing import Any

from algoneer.object import Object

import abc


class Result(Object, abc.ABC):
    def __init__(self, data: Any):
        super().__init__()
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
