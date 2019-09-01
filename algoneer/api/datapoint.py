from .object import Object
from .manager import Manager
from algoneer.dataset import Datapoint as ADatapoint

from typing import Dict, Any


class Datapoint(Object):
    Type = ADatapoint

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Datapoints(Manager[Datapoint]):
    Type = Datapoint
