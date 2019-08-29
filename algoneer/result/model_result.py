import algoneer
from .result import Result
from .datapoint_model_result import DatapointModelResult

from typing import Any, Optional, Iterable


class ModelResult(Result):

    """
    Contains a result for a given model, and optionally results for individual
    datapoints for the model.
    """

    def __init__(
        self,
        data: Any,
        model: "algoneer.Model",
        datapoint_results: Optional[Iterable[DatapointModelResult]] = None,
    ):
        super().__init__(data)
        self.model = model
        self.datapoint_results = datapoint_results
