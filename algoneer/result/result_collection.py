from typing import Dict, Union, Iterable
from .result import Result


class ResultCollection:
    def __init__(self, collection=Dict[str, Result]) -> None:
        self._collection = collection

    @property
    def collection(self):
        return self._collection

    def __getitem__(self, key: str) -> Result:
        return self._collection[key]

    def __setitem__(self, key: str, value: Result):
        self._collection[key] = value
