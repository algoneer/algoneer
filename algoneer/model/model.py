import abc

from algoneer.dataset import Dataset, Attribute
from algoneer.result import Result
from algoneer.algorithm import Algorithm

from typing import Union, Dict


class Model(abc.ABC):
    def __init__(self, algorithm: Algorithm) -> None:
        self._algorithm = algorithm

    def test(self, dataset: Dataset) -> Dict[str, Result]:
        results: Dict[str, Result] = {}
        return results

    @abc.abstractmethod
    def predict(self, dataset: Dataset) -> Union[Dataset, Attribute]:
        pass

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
