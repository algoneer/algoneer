import abc

from algoneer.dataset import DataSet, Attribute
from algoneer.algorithm import Algorithm

from typing import Union


class Model(abc.ABC):
    def __init__(self, algorithm: Algorithm) -> None:
        self._algorithm = algorithm

    @abc.abstractmethod
    def predict(self, dataset: DataSet) -> Union[DataSet, Attribute]:
        pass

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
