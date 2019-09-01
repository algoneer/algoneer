import abc
import logging

from algoneer.result import DatasetModelResult
from algoneer.model import Model
from algoneer.dataset import Dataset

from typing import Mapping, Any, Iterable, Optional


class DatasetModelTest(abc.ABC):
    def __init__(self) -> None:
        self.logger: logging.Logger = logging.getLogger(__name__)

    @abc.abstractmethod
    def run(self, dataset: Dataset, model: Model, **kwargs) -> DatasetModelResult:
        pass

    def log(self, level: int, message: str, **kwargs):
        message = "[{}]: {}".format(self.__class__.__name__, message)
        self.logger.log(level, message, **kwargs)
