import logging

from algoneer.modeltest import ModelTest

from typing import List, Type

from .ale import ALE
from .pdp import PDP
from .predictions import Predictions

model_tests: List[Type[ModelTest]] = [ALE, PDP, Predictions]

logger = logging.getLogger(__name__)

# These are optional tests that require additional dependencies, Algoneer works without them as
# well though
try:
    from .shap import SHAP
except ImportError:
    logger.debug("Importing SHAP test failed, skipping...")
    pass

model_tests.append(SHAP)
