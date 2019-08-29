import logging

from .ale import ALE
from .pdp import PDP
from .predictions import Predictions

logger = logging.getLogger(__name__)

# These are optional tests that require additional dependencies, Algoneer works without them as
# well though
try:
    from .shap import SHAP
except ImportError:
    logger.debug("Importing SHAP test failed, skipping...")
    pass
