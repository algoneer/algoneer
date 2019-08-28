import algoneer
from .result import Result

from typing import Any


class ModelResult(Result):
    def __init__(self, data: Any, model: "algoneer.Model"):
        super().__init__(data)
        self.model = model
