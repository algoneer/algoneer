import abc

from typing import Any, Dict, Union, Iterable


class Result:
    def __init__(self, data: Any):
        self._data = data

    @property
    def data(self) -> Any:
        return self._data

    def format(self, format: str) -> Any:
        pass


class ResultCollection:
    def __init__(self, collection=Dict[str, Union[Result, Iterable[Result]]]) -> None:
        self._collection = collection

    @property
    def collection(self):
        return self._collection

    def __getitem__(self, key: str) -> Union[Result, Iterable[Result]]:
        return self._collection[key]

    def __setitem__(self, key: str, value: Union[Result, Iterable[Result]]):
        self._collection[key] = value
