import algoneer
from .result import Result

from typing import Any


class DatasetResult(Result):
    def __init__(self, data: Any, dataset: "algoneer.Dataset"):
        super().__init__(data)
        self.dataset = dataset
