from .object import Object
from .manager import Manager
from algoneer.result import DatasetResult as ADatasetResult

from typing import Dict, Any


class DatasetResult(Object):
    Type = ADatasetResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class DatasetResults(Manager[DatasetResult]):
    Type = DatasetResult
