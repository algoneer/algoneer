from .result import Result
import algoneer

from typing import Dict, Any


class DatapointModelResult(Result):
    def __init__(
        self,
        data: Dict[str, Any],
        datapoint: "algoneer.Datapoint",
        model: "algoneer.Model",
    ):
        super().__init__(data)
        self.datapoint = datapoint
        self.model = model
