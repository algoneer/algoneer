from .object import Object
from .manager import Manager
from algoneer.result import DatasetModelResult as ADatasetModelResult

from typing import Dict, Any


class DatasetModelResult(Object):
    Type = ADatasetModelResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class DatasetModelResults(Manager[DatasetModelResult]):
    Type = DatasetModelResult
