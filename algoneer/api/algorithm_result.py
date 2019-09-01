from .object import Object
from .manager import Manager
from algoneer.result import AlgorithmResult as AAlgorithmResult

from typing import Dict, Any, Optional


class AlgorithmResult(Object):
    Type = AAlgorithmResult

    @property
    def dependencies(self):
        return [self.obj.algorithm]


class AlgorithmResults(Manager[AlgorithmResult]):
    Type = AlgorithmResult

    def url(self, obj: Optional[AlgorithmResult]) -> str:
        return ""
