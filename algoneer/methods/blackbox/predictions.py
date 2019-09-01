"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Iterable, Any, Dict
from algoneer import Dataset, Model, DatasetModelTest, Attribute, Datapoint
from algoneer.result import DatasetModelResult, DatapointModelResult, Result


class PredictionsDatapointResult(Result):
    @property
    def name(self):
        return "predictions.datapoint"

    @property
    def version(self):
        return "1.0.0"


class PredictionsResult(Result):
    @property
    def name(self):
        return "predictions.model"

    @property
    def version(self):
        return "1.0.0"


class Predictions(DatasetModelTest):

    """
    Generates a list of predictions for a given model.
    """

    def __init__(self):
        super().__init__()

    def run(self, dataset: Dataset, model: Model, **kwargs) -> DatasetModelResult:
        max_datapoints = kwargs.get("max_datapoints", None)
        Y = model.predict(dataset)
        results = []
        for y in Y:
            ind, pred = y
            dp = dataset.datapoint(ind)
            results.append(
                DatapointModelResult(
                    dp, model, PredictionsDatapointResult({"p": float(pred)})
                )
            )

        return DatasetModelResult(dataset, model, PredictionsResult({}), results)
