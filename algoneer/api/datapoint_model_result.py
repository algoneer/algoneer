from .object import Object
from .objects import Objects
from algoneer.result import DatapointModelResult as ADatapointModelResult


class DatapointModelResult(Object):
    Type = ADatapointModelResult


class DatapointModelResults(Objects[DatapointModelResult]):
    Type = DatapointModelResult
