from .result import Result, ResultProxy
from algoneer.dataset import Dataset
from algoneer.model import Model
from algoneer.object import Object


class DatasetResult(Object, ResultProxy):
    def __init__(self, dataset: Dataset, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._dataset = dataset
