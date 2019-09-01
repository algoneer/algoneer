import abc

from algoneer.object import Object
from algoneer.utils.hashing import get_hash
from algoneer.dataset import Dataset, Attribute
from algoneer.algorithm import Algorithm

from typing import Union, Dict, Iterable, Dict, Any, Optional


class Model(Object, abc.ABC):
    def __init__(self, algorithm: Algorithm, dataset: Optional[Dataset] = None) -> None:
        super().__init__()
        self._algorithm = algorithm
        self._dataset = dataset

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
    def dataset(self) -> Optional[Dataset]:
        return self._dataset

    @property
    def algorithm(self) -> Algorithm:
        return self._algorithm
