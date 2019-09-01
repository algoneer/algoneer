from .object import Object
from .objects import Objects
from algoneer.dataset import Datapoint as ADatapoint


class Datapoint(Object):
    Type = ADatapoint


class Datapoints(Objects[Datapoint]):
    Type = Datapoint
