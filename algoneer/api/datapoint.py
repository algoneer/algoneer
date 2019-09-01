from .object import Object
from .manager import Manager
from algoneer.dataset import Datapoint as ADatapoint


class Datapoint(Object):
    Type = ADatapoint


class Datapoints(Manager[Datapoint]):
    Type = Datapoint
