from .result import Result
import algoneer

from typing import Any


class DatapointModelResult(Result):
    def __init__(
        self, data: Any, datapoint: "algoneer.Datapoint", model: "algoneer.Model"
    ):
        super().__init__(data)
        self.datapoint = datapoint
        self.model = model
