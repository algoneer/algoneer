from .object import Object
from .manager import Manager
from algoneer.model.model import Model as AModel


class Model(Object):
    Type = AModel


class Models(Manager[Model]):
    Type = Model
