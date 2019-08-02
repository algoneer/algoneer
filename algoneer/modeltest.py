import logging

from typing import Mapping, Any, Iterable


class ModelTest:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    def log(self, level: int, message: str, **kwargs):
        message = "[{}]: {}".format(self.__class__.__name__, message)
        self.logger.log(level, message, **kwargs)
