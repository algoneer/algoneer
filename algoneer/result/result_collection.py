from typing import Dict, Union, Iterable
from .result import ResultProxy


class ResultCollection:
    def __init__(self, collection=Dict[str, ResultProxy]) -> None:
        self._collection = collection

    @property
    def collection(self):
        return self._collection

    def __getitem__(self, key: str) -> ResultProxy:
        return self._collection[key]

    def __setitem__(self, key: str, value: ResultProxy):
        self._collection[key] = value
