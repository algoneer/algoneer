from .object import APIObject
from algoneer.result import Result, ResultCollection


class APIResult(APIObject):
    def __init__(self, result: Result) -> None:
        self._result = result


class APIResultCollection(APIObject):
    def __init__(self, collection: ResultCollection) -> None:
        self._collection = collection
