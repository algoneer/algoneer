from algoneer.dataschema import DataSchema
from .roles import Roles
from .attribute import Attribute

import abc

from typing import Iterable, Mapping, Tuple, Union


class Datapoint(abc.ABC):

    """Describes a single datapoint.
    """

    @property
    def roles(self):
        return Roles(self)

    @property
    @abc.abstractmethod
    def columns(self) -> Iterable[str]:
        pass

    @property
    @abc.abstractmethod
    def attributes(self) -> Mapping[str, Attribute]:
        pass

    @property  # type: ignore
    def schema(self) -> DataSchema:
        pass

    @schema.setter  # type: ignore
    def schema(self, schema: DataSchema) -> None:
        pass

    @abc.abstractmethod
    def __getitem__(self, item) -> Union["Datapoint", Attribute]:
        pass

    @abc.abstractmethod
    def __setitem__(self, item, value):
        pass

    @abc.abstractmethod
    def __delitem__(self, item):
        pass

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def __sub__(self, other: "Datapoint") -> "Datapoint":
        pass

    @abc.abstractmethod
    def __add__(self, other: "Datapoint") -> "Datapoint":
        pass

    @abc.abstractmethod
    def copy(self) -> "Datapoint":
        pass

    @property  # type: ignore
    @abc.abstractmethod
    def shape(self) -> Tuple:
        pass

    @abc.abstractmethod
    def select(self, indexes: Union[Iterable[int], slice]) -> "Datapoint":
        pass

    @abc.abstractmethod
    def sum(self) -> float:
        pass

    @abc.abstractmethod
    def mean(self) -> float:
        pass

    @abc.abstractmethod
    def order_by(self, columns: Iterable[str]) -> "Datapoint":
        pass
