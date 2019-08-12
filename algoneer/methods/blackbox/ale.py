"""
algoneer.methods.blackbox.ALE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of accumulated local effects for machine
learning models.
"""

from typing import Sequence, Optional, Dict, Any, List, Iterable, Tuple, Union
from algoneer import DataSet, Model, ModelTest, Attribute

from collections import defaultdict

import logging


class ALE(ModelTest):

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
        n_intervals: int = 10,
        max_datapoints: int = None,
        correlated: bool = False,
    ) -> Dict[str, List[Tuple[float, float, float]]]:
        """
        Run the test.

        :param    model: The model for which to generate the ALE.
        :param  dataset: The dataset for which to generate the ALE.
        :param columns: The columns for which to generate the ALE. Optional.
        """

        cvs: Dict[str, Iterable[Any]] = {}

        def ALE(
            ds: DataSet, model: Model, column: str
        ) -> List[Tuple[float, float, float]]:

            ys: List[Tuple[float, float, float]] = []

            ndo = nds.order_by([column])
            m = len(ndo) // n_intervals

            i = 0

            ales = []

            for i in range(n_intervals):
                # we select all datapoints from the given interval
                vs = ndo.select(slice(i * m, (i + 1) * m))
                vc = vs[column]
                assert isinstance(vc, Attribute)
                min_v = vc.min()
                max_v = vc.max()
                if min_v == max_v:
                    ales.append((min_v, max_v, 0.0))
                    continue
                vs[column] = min_v
                y_min = model.predict(vs)
                assert isinstance(y_min, DataSet)
                vs[column] = max_v
                y_max = model.predict(vs)
                assert isinstance(y_max, DataSet)
                dy = float((y_max - y_min).mean())
                dx = max_v - min_v
                ales.append((min_v, max_v, dy))
                # we replace

            summed_ales = []
            for i in range(len(ales)):
                s = 0.0
                for j in range(i + 1):
                    s += ales[j][2]
                summed_ales.append((ales[i][0], ales[i][1], s))

            mean = sum([v[2] for v in summed_ales]) / len(summed_ales)
            centered_ales = [(v[0], v[1], v[2] - mean) for v in summed_ales]

            return centered_ales

        # we make a copy of the dataset (this might be expensive)
        nds = dataset.copy()

        if max_datapoints is not None and nds.shape[0] > max_datapoints:
            indexes: List[int] = [0]
            for i in range(1, max_datapoints):
                indexes.append((i * len(nds)) // max_datapoints - 1)
            nds = nds.select(indexes)

        ALEs: Dict[str, List[Tuple[float, float, float]]] = {}
        for column in nds.columns:
            if columns is not None and not column in columns:
                continue
            attribute = dataset[column]

            # we ensure this is an attribute
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

            ALEs[column] = ALE(nds, model, column)
        return ALEs
