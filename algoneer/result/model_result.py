import algoneer
from .result import Result

from typing import Dict, Any


class ModelResult(Result):
    def __init__(self, data: Dict[str, Any], model: "algoneer.Model"):
        super().__init__(data)
        self.model = model
