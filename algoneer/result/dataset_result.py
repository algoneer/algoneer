from .result import Result, ResultProxy
from algoneer.dataset import Dataset
from algoneer.model import Model
from algoneer.object import Object

from typing import Dict, Any


class DatasetResult(Object, ResultProxy):
    def __init__(self, dataset: Dataset, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._dataset = dataset

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
