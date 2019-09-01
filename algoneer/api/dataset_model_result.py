from .object import Object
from .manager import Manager
from algoneer.result import DatasetModelResult as ADatasetModelResult

from typing import Dict, Any, Optional


class DatasetModelResult(Object):
    Type = ADatasetModelResult

    @property
    def dependencies(self):
        return [self.obj.dataset, self.obj.model, self.obj.result]


class DatasetModelResults(Manager[DatasetModelResult]):
    Type = DatasetModelResult

    def url(self, obj: Optional[DatasetModelResult]) -> str:
        return ""
