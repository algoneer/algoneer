from .object import Object
from .manager import Manager
from algoneer.result import ModelResult as AModelResult


class ModelResult(Object):
    Type = AModelResult


class ModelResults(Manager[ModelResult]):
    Type = ModelResult
