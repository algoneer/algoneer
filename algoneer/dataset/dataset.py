from algoneer.dataschema import DataSchema
from .roles import Roles
import abc


class DataSet(abc.ABC):

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
    """

    @property
    @abc.abstractmethod
    def roles(self) -> Roles:
        pass

    @abc.abstractmethod
    def validate(self) -> bool:
        pass

    @property
    @abc.abstractmethod
    def attributes(self):
        return self._attributes

    @property  # type: ignore
    @abc.abstractmethod
    def schema(self) -> DataSchema:
        pass

    @schema.setter  # type: ignore
    @abc.abstractmethod
    def schema(self, schema: DataSchema) -> None:
        pass
