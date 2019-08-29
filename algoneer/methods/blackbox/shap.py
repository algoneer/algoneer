"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

import shap
from typing import Iterable, Tuple
from algoneer import Dataset, Model, ModelTest, Attribute, Datapoint
from algoneer.result import DatapointModelResult, ModelResult


class SHAPDatapointResult(DatapointModelResult):
    pass


class SHAPModelResult(ModelResult):
    pass


class SHAP(ModelTest):

    """
    Generates SHAP explanations for a machine learning model.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, model: Model, dataset: Dataset, max_datapoints: int = None
    ) -> SHAPModelResult:
        npd = dataset.roles.x.df
        explainer = shap.KernelExplainer(model.predict, npd[:10])
        shap_values = explainer.shap_values(
            npd[:max_datapoints], l1_reg="num_features(10)"
        )
        ex = float(explainer.expected_value)
        dp_results = []
        for i, shap_value in enumerate(shap_values):
            dp_results.append(
                SHAPDatapointResult(shap_value, dataset.datapoint(i), model)
            )
        return SHAPModelResult(
            {"expected_value": ex, "shap_values": shap_values}, model, dp_results
        )
