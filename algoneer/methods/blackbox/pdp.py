"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Sequence, Optional, Dict, Any, List, Iterable
from algoneer import DataSet, Model, ModelTest

from collections import defaultdict

import logging


class PDP(ModelTest):

    """
    Generates a partial dependence plots for a model.
    """

    def __init__(self):
        super().__init__()

    def run(
        self,
        model: Model,
        dataset: DataSet,
        columns: Optional[Sequence[str]] = None,
        max_values: int = None,
        max_datapoints: int = None,
    ):
        """
        Run the test.

        :param    model: The model for which to generate the PDP.
        :param  dataset: The dataset for which to generate the PDP.
        :param columns: The columns for which to generate the PDP. Optional.
        """

        cvs: Dict[str, Iterable[Any]] = {}

        for column in dataset.roles.x.columns:
            if columns is not None and not column in columns:
                continue
            attribute = dataset[column]
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
                vss = [0]
                # we pick quantile values for the test
                for i in range(1, max_values + 1):
                    vss.append(vs[i * len(vs) // max_values - 1])
                vs = vss

            cvs[column] = vs

        def pdp(ds, model, column_a, column_b):
            """
            Generate the partial dependence for a categorical attribute
            """

            ys = []

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

                    ys.append((va, vb, py))

            return ys

        # we store PDPs in a simple dict
        pdps: Dict[str, Dict[str, Any]] = defaultdict(dict)

        # we make a copy of the dataset (this might be expensive)
        nds = dataset.copy()

        if max_datapoints is not None and nds.shape[0] > max_datapoints:
            indexes: List[int] = [0]
            for i in range(1, max_datapoints):
                indexes.append((i * len(nds)) // max_datapoints - 1)
            nds = nds.select(indexes)

        # we generate a partial dependence plot for every column
        for column_a in dataset.roles.x.columns:
            if columns is not None and not column_a in columns:
                continue
            for column_b in dataset.roles.x.columns:
                if columns is not None and not column_b in columns:
                    continue
                if not column_a in cvs or not column_b in cvs:
                    continue
                pdps[column_a][column_b] = pdp(nds, model, column_a, column_b)

        # we return the PDPs
        return pdps
