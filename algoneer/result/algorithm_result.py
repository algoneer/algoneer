import algoneer
from .result import Result

from typing import Any


class AlgorithmResult(Result):
    def __init__(self, data: Any, algorithm: "algoneer.Algorithm"):
        super().__init__(data)
        self.algorithm = algorithm
