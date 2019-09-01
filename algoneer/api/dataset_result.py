from .object import Object
from .manager import Manager
from algoneer.result import DatasetResult as ADatasetResult


class DatasetResult(Object):
    Type = ADatasetResult


class DatasetResults(Manager[DatasetResult]):
    Type = DatasetResult
