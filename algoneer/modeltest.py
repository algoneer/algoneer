import abc
import logging

from algoneer.result import ModelResult
from algoneer.model import Model
from algoneer.dataset import Dataset

from typing import Mapping, Any, Iterable, Optional


class ModelTest(abc.ABC):
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def run(self, model: Model, dataset: Dataset, **kwargs) -> ModelResult:
        pass

    def log(self, level: int, message: str, **kwargs):
        message = "[{}]: {}".format(self.__class__.__name__, message)
        self.logger.log(level, message, **kwargs)
