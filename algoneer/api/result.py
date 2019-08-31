from .object import Object
from algoneer.result import Result as AResult, ResultCollection as AResultCollection


class Result(Object):
    def __init__(self, result: AResult) -> None:
        self._result = result


class ResultCollection(Object):
    def __init__(self, collection: AResultCollection) -> None:
        self._collection = collection
