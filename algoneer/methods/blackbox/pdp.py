"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Sequence
from algoneer import DataSet, Model, ModelTest


class PDP(ModelTest):

    """
    Generates partial dependence plots for a model.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, model: Model, dataset: DataSet = None, features: Sequence[str] = None
    ):
        pass
