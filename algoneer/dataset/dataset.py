from algoneer.dataschema import DataSchema
from .roles import Roles
from .datapoint import Datapoint
from .attribute import Attribute
import abc

from typing import Iterable, Mapping, Tuple, Union, Any, Iterator


class Dataset(abc.ABC):

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
    """

    def __init__(self, schema: DataSchema) -> None:
        self._schema = schema

    @property
    def roles(self):
        return Roles(self)

    @abc.abstractmethod
    def datapoint(self, index: Any) -> Datapoint:
        pass

    @property
    @abc.abstractmethod
    def columns(self) -> Iterable[str]:
        pass

    @property
    @abc.abstractmethod
    def attributes(self) -> Mapping[str, Attribute]:
        pass

    @property
    def schema(self) -> DataSchema:
        return self._schema

    @schema.setter
    def schema(self, schema: DataSchema) -> None:
        self._schema = schema

    @abc.abstractmethod
    def __getitem__(self, item) -> Union["Dataset", Attribute]:
        pass

    @abc.abstractmethod
    def __setitem__(self, item, value):
        pass

    @abc.abstractmethod
    def __delitem__(self, item):
        pass

    @abc.abstractmethod
    def __iter__(self) -> Iterator:
        pass

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def __sub__(self, other: "Dataset") -> "Dataset":
        pass

    @abc.abstractmethod
    def __add__(self, other: "Dataset") -> "Dataset":
        pass

    @abc.abstractmethod
    def copy(self) -> "Dataset":
        pass

    @property
    @abc.abstractmethod
    def shape(self) -> Tuple:
        pass

    @abc.abstractmethod
    def select(self, indexes: Union[Iterable[int], slice]) -> "Dataset":
        pass

    @abc.abstractmethod
    def sum(self) -> float:
        pass

    @abc.abstractmethod
    def mean(self) -> float:
        pass

    @abc.abstractmethod
    def order_by(self, columns: Iterable[str]) -> "Dataset":
        pass
