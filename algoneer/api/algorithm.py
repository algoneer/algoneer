from .object import Object
from .manager import Manager
from algoneer.algorithm import Algorithm as AAlgorithm

from typing import Dict, Any


class Algorithm(Object):
    Type = AAlgorithm

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Algorithms(Manager[Algorithm]):
    Type = Algorithm
