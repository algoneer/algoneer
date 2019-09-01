import logging

from algoneer.utils import CI
from algoneer import DatasetModelTest

from typing import List, Type

from .ale import ALE
from .pdp import PDP
from .predictions import Predictions

dataset_model_tests: List[Type[DatasetModelTest]] = [ALE, PDP, Predictions]

logger = logging.getLogger(__name__)

# Only raises an exception if the "shap" module is available, otherwise silently discards
# the import with a log message that the module is not available...
with CI("shap"):
    from .shap import SHAP

    dataset_model_tests.append(SHAP)
