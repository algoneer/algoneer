from .object import Object
from .manager import Manager
from algoneer.algorithm import Algorithm as AAlgorithm

from typing import Dict, Any, Optional


class Algorithm(Object):
    Type = AAlgorithm

    @property
    def dependencies(self):
        return [self.obj.project, self.obj.schema]


class Algorithms(Manager[Algorithm]):
    Type = Algorithm

    def url(self, obj: Optional[Algorithm]) -> str:
        return ""
