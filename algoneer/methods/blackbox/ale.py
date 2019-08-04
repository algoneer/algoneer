"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Sequence, Optional, Dict, Any, List, Iterable, Tuple, Union
from algoneer import DataSet, Model, ModelTest

from collections import defaultdict

import logging


class ALE(ModelTest):

    """
    Generates accumulated local effects estimates for a model.
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

        """
        Strategy:

        - For each attribute, generate a list of quantile intervals.
        - For each quantile interval, select all datapoints from the interval.
        """
