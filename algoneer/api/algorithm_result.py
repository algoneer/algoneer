from .object import Object
from .manager import Manager
from algoneer.result import AlgorithmResult as AAlgorithmResult


class AlgorithmResult(Object):
    Type = AAlgorithmResult


class AlgorithmResults(Manager[AlgorithmResult]):
    Type = AlgorithmResult
