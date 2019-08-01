from algoneer.dataschema import DataSchema
from .roles import Roles
from .attribute import Attribute
import abc

from typing import Iterable, Mapping


class DataSet(abc.ABC):

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
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
    def __getitem__(self, item):
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
