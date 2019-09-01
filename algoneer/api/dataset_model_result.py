from .object import Object
from .manager import Manager
from algoneer.result import DatasetModelResult as ADatasetModelResult


class DatasetModelResult(Object):
    Type = ADatasetModelResult


class DatasetModelResults(Manager[DatasetModelResult]):
    Type = DatasetModelResult
