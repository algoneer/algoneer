from .object import Object
from .manager import Manager
from algoneer.result import DatasetResult as ADatasetResult

from typing import Dict, Any, Optional


class DatasetResult(Object):
    Type = ADatasetResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class DatasetResults(Manager[DatasetResult]):
    Type = DatasetResult

    def url(self, obj: Optional[DatasetResult]) -> str:
        return ""
