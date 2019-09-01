from .object import Object
from .manager import Manager
from algoneer.result import DatapointModelResult as ADatapointModelResult


class DatapointModelResult(Object):
    Type = ADatapointModelResult


class DatapointModelResults(Manager[DatapointModelResult]):
    Type = DatapointModelResult
