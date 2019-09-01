from .object import Object
from .manager import Manager
from algoneer.result import DatapointModelResult as ADatapointModelResult

from typing import Dict, Any, Optional


class DatapointModelResult(Object):
    Type = ADatapointModelResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class DatapointModelResults(Manager[DatapointModelResult]):
    Type = DatapointModelResult

    def url(self, obj: Optional[DatapointModelResult]) -> str:
        return ""
