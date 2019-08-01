import logging

from typing import Mapping, Any, Iterable


class ModelTest:
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    def log(self, level: int, *args, **kwargs):
        self.logger.log(level, *args, **kwargs)
