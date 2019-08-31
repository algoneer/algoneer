import abc

from algoneer.object import Object
from algoneer.utils.hashing import get_hash
from algoneer.dataset import Dataset, Attribute
from algoneer.result import Result, ResultCollection
from algoneer.algorithm import Algorithm

from typing import Union, Dict, Iterable, Dict, Any


class Model(Object, abc.ABC):
    def __init__(self, algorithm: Algorithm) -> None:
        super().__init__()
        self._algorithm = algorithm

    def test(self, dataset: Dataset) -> ResultCollection:
        results: Dict[str, Union[Result, Iterable[Result]]] = {}
        return ResultCollection(results)

    @abc.abstractproperty
    def data(self) -> Dict[str, Any]:
        pass

    @property
    def hash(self) -> bytes:
        return get_hash(self.data)

    @abc.abstractmethod
    def predict(self, dataset: Dataset) -> Dataset:
        pass

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
