from .object import Object
from .manager import Manager
from algoneer.algorithm import Algorithm as AAlgorithm


class Algorithm(Object):
    Type = AAlgorithm


class Algorithms(Manager[Algorithm]):
    Type = Algorithm
