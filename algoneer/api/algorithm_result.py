from .object import Object
from .manager import Manager
from algoneer.result import AlgorithmResult as AAlgorithmResult

from typing import Dict, Any


class AlgorithmResult(Object):
    Type = AAlgorithmResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class AlgorithmResults(Manager[AlgorithmResult]):
    Type = AlgorithmResult
