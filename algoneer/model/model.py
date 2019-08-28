import abc

from algoneer.dataset import Dataset, Attribute
from algoneer.result import Result
from algoneer.algorithm import Algorithm

from typing import Union, Dict, Iterable


class Model(abc.ABC):
    def __init__(self, algorithm: Algorithm) -> None:
        self._algorithm = algorithm

    def test(self, dataset: Dataset) -> Dict[str, Union[Result, Iterable[Result]]]:
        results: Dict[str, Union[Result, Iterable[Result]]] = {}
        return results

    @abc.abstractmethod
    def predict(self, dataset: Dataset) -> Dataset:
        pass

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
