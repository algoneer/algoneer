from .object import Object
from .objects import Objects
from algoneer.result import DatasetModelResult as ADatasetModelResult


class DatasetModelResult(Object):
    Type = ADatasetModelResult


class DatasetModelResults(Objects[DatasetModelResult]):
    Type = DatasetModelResult
