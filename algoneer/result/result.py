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


class ResultProxy:
    def __init__(self, result: Result) -> None:
        self._result = result

    @property
    def result(self) -> Result:
        return self._result

    @property
    def name(self) -> str:
        return self.result.name

    @property
    def version(self) -> str:
        return self.result.version

    @property
    def data(self) -> Any:
        return self.result.data

    def format(self, format: str) -> Any:
        return self.result.format
