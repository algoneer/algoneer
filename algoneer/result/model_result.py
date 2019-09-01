from .result import Result, ResultProxy
from algoneer.model import Model
from algoneer.model import Model
from algoneer.object import Object

from typing import Dict, Any


class ModelResult(Object, ResultProxy):
    def __init__(self, model: Model, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._model = model

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
