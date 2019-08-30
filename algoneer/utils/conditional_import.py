import importlib
import logging

logger = logging.getLogger(__name__)


class CI:
    def __init__(self, module):
        self.module = module

    def __enter__(self):
        try:
            importlib.import_module(self.module)
            self.module_available = True
        except ModuleNotFoundError:
            self.module_available = False

    def __exit__(self, type, value, traceback):
        if type == ModuleNotFoundError and not self.module_available:
            logger.debug(
                "Module '{}' is not available, discarding import error...".format(
                    self.module
                )
            )
            return True
