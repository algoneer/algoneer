from .object import Object
from .manager import Manager
from algoneer.result import DatasetResult as ADatasetResult

from typing import Dict, Any, Optional


class DatasetResult(Object):
    Type = ADatasetResult

    @property
    def dependencies(self):
        return [self.mapped_obj.dataset]


class DatasetResults(Manager[DatasetResult]):
    Type = DatasetResult

    def url(self, obj: DatasetResult) -> str:
        return ""
