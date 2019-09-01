from .result import Result, ResultProxy
from algoneer.dataset import Datapoint
from algoneer.model import Model
from algoneer.object import Object

from typing import Dict, Any


class DatapointModelResult(Object, ResultProxy):
    def __init__(self, datapoint: Datapoint, model: Model, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._datapoint = datapoint
        self._model = model

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
