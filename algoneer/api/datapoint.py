from .object import Object
from .manager import Manager
from algoneer.dataset import Datapoint as ADatapoint

from typing import Dict, Any, Optional


class Datapoint(Object):
    Type = ADatapoint

    @property
    def dependencies(self):
        return [self.obj.dataset]


class Datapoints(Manager[Datapoint]):
    Type = Datapoint

    def url(self, obj: Optional[Datapoint]) -> str:
        return ""
