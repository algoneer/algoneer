from .object import Object
from .manager import Manager
from algoneer.result import DatapointModelResult as ADatapointModelResult

from typing import Dict, Any, Optional


class DatapointModelResult(Object):
    Type = ADatapointModelResult

    @property
    def dependencies(self):
        return [self.mapped_obj.datapoint, self.mapped_obj.model]


class DatapointModelResults(Manager[DatapointModelResult]):
    Type = DatapointModelResult

    def url(self, obj: DatapointModelResult) -> str:
        return ""
