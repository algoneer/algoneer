"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Sequence, Optional, Dict, Any, List, Iterable, Tuple, Union
from algoneer import Dataset, Model, DatasetModelTest, Attribute
from algoneer.result import DatasetModelResult, Result

from collections import defaultdict

import logging


class PDPResult(Result):
    @property
    def name(self):
        return "pdp"

    @property
    def version(self):
        return "1.0.0"


class PDP(DatasetModelTest):

    """
    Generates a partial dependence plots for a model.
    """

    def __init__(self):
        super().__init__()

    def run(self, dataset: Dataset, model: Model, **kwargs) -> DatasetModelResult:
        """
        Run the test.

        :param  dataset: The dataset for which to generate the PDP.
        :param    model: The model for which to generate the PDP.
        :param columns: The columns for which to generate the PDP. Optional.
        """

        columns: Optional[Sequence[str]] = kwargs.get("columns", None)
        max_values: Optional[int] = kwargs.get("max_values", None)
        max_datapoints: Optional[int] = kwargs.get("max_datapoints", None)
        correlated: Optional[bool] = kwargs.get("correlated", False)

        cvs: Dict[str, Iterable[Any]] = {}

        for column in dataset.roles.x.columns:
            if columns is not None and not column in columns:
                continue
            attribute = dataset[column]
            assert isinstance(attribute, Attribute)
            if attribute.is_categorical or attribute.is_ordinal:
                # we get all unique values for the attribute
                vs = sorted(attribute.unique())
            elif attribute.is_numerical:
                vs = sorted(attribute.unique())
            else:
                self.log(
                    logging.WARNING,
                    "unknown attribute type for column '{}', skipping...".format(
                        attribute.column
                    ),
                )
                continue

            if max_values is not None and len(vs) > max_values:
                vss = [vs[0]]
                # we pick quantile values for the test
                for i in range(1, max_values):
                    vss.append(vs[i * len(vs) // max_values - 1])
                vs = vss

            cvs[column] = vs

        def pdp(ds: Dataset, model: Model, column: str) -> List[Tuple[float, float]]:

            ys: List[Tuple[float, float]] = []

            for v in cvs[column]:
                # we replace all values of the attribute by v
                old_column = nds[column].copy()
                nds[column] = v
                # we compute the prediction of the model for the modified data
                y = model.predict(nds)
                if model.algorithm.is_classifier:
                    # to do: handle multi-class classifiers
                    # if this is a classifier we calculate the probability
                    py = float(y.sum() / len(y))
                elif model.algorithm.is_regressor:
                    # if this is a regression, we calculate the mean value
                    py = float(y.mean())

                # we revert the columns to their old values
                nds[column] = old_column

                ys.append((v, py))

            return ys

        def pdp_correlated(
            ds: Dataset, model: Model, column_a: str, column_b: str
        ) -> List[Tuple[float, float, float]]:
            """
            Generate the partial dependence for a categorical attribute
            """

            ys: List[Tuple[float, float, float]] = []

            for va in cvs[column_a]:
                for vb in cvs[column_b]:
                    # we replace all values of the attribute by v
                    old_column_a = nds[column_a].copy()
                    old_column_b = nds[column_b].copy()
                    nds[column_a] = va
                    nds[column_b] = vb
                    # we compute the prediction of the model for the modified data
                    y = model.predict(nds)
                    if model.algorithm.is_classifier:
                        # to do: handle multi-class classifiers
                        # if this is a classifier we calculate the probability
                        py = float(y.sum() / len(y))
                    elif model.algorithm.is_regressor:
                        # if this is a regression, we calculate the mean value
                        py = float(y.mean())

                    # we revert the columns to their old values
                    nds[column_a] = old_column_a
                    nds[column_b] = old_column_b

                    ys.append((float(va), float(vb), py))

            return ys

        # we make a copy of the dataset (this might be expensive)
        nds = dataset.copy()

        if max_datapoints is not None and nds.shape[0] > max_datapoints:
            indexes: List[int] = [0]
            for i in range(1, max_datapoints):
                indexes.append((i * len(nds)) // max_datapoints - 1)
            nds = nds.select(indexes)

        if correlated:

            # we store PDPs in a simple dict
            correlated_pdps: Dict[
                str, Dict[str, List[Tuple[float, float, float]]]
            ] = defaultdict(dict)

            # we generate a partial dependence plot for every column
            for column_a in cvs:
                if columns is not None and not column_a in columns:
                    continue
                for column_b in cvs:
                    if columns is not None and not column_b in columns:
                        continue
                    if not column_a in cvs or not column_b in cvs:
                        continue
                    correlated_pdps[column_a][column_b] = pdp_correlated(
                        nds, model, column_a, column_b
                    )
            result = PDPResult(correlated_pdps)
        else:

            pdps: Dict[str, List[Tuple[float, float]]] = {}
            for column in cvs:
                if columns is not None and not column in columns:
                    continue
                pdps[column] = pdp(nds, model, column)
            result = PDPResult(pdps)
        return DatasetModelResult(dataset, model, result)
