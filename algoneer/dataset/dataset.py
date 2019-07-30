from algoneer.dataschema import DataSchema
from .roles import Roles
import abc

from typing import Iterable


class DataSet(abc.ABC):

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
    """

    @property
    @abc.abstractmethod
    def roles(self) -> Roles:
        pass

    @property
    @abc.abstractmethod
    def columns(self) -> Iterable[str]:
        pass

    @property  # type: ignore
    @abc.abstractmethod
    def schema(self) -> DataSchema:
        pass

    @schema.setter  # type: ignore
    @abc.abstractmethod
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
    def __getattr__(self, attr):
        pass

    @abc.abstractmethod
    def __setattr__(self, attr, value):
        pass
