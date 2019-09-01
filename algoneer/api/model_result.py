from .object import Object
from .manager import Manager
from algoneer.result import ModelResult as AModelResult

from typing import Dict, Any


class ModelResult(Object):
    Type = AModelResult

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class ModelResults(Manager[ModelResult]):
    Type = ModelResult
