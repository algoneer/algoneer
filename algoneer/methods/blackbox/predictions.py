"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Iterable, Any, Dict
from algoneer import Dataset, Model, ModelTest, Attribute, Datapoint
from algoneer.result import DatapointModelResult, Result

from collections import defaultdict

import logging


class PredictionsResult(Result):
    @property
    def data(self) -> Dict[str, Any]:
        return {}

    def format(self, format: str) -> Any:
        return ""


class Predictions(ModelTest):

    """
    Generates a list of predictions for a given model.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, model: Model, dataset: Dataset, max_datapoints: int = None
    ) -> Iterable[DatapointModelResult]:
        Y = model.predict(dataset)
        results = []
        for y in Y:
            ind, pred = y
            dp = dataset.datapoint(ind)
            results.append(DatapointModelResult({"pred": float(pred)}, dp, model))

        return results
