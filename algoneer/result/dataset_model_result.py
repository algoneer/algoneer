from algoneer.object import Object
from algoneer.dataset import Dataset
from algoneer.model import Model
from typing import Any, Dict, Optional, Iterable
from .result import ResultProxy, Result
from .datapoint_model_result import DatapointModelResult


class DatasetModelResult(Object, ResultProxy):

    """
    Relates a model
    """

    def __init__(
        self,
        dataset: Dataset,
        model: Model,
        result: Result,
        datapoint_results: Optional[Iterable[DatapointModelResult]] = None,
    ):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._dataset = dataset
        self._model = model
        self._datapoint_results = datapoint_results

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
