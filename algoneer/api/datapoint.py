from .object import Object
from .objects import Objects


class Datapoint(Object):
    pass


class Datapoints(Objects[Datapoint]):
    Type = Datapoint
