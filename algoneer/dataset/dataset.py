from algoneer.dataschema import DataSchema
from algoneer.object import Object
from algoneer.project import Project
from .roles import Roles
from .datapoint import Datapoint
from .attribute import Attribute
import abc

from typing import Iterable, Mapping, Tuple, Union, Any, Iterator, Optional


class Dataset(Object, abc.ABC):

    """Describes a collection of datapoints.
    """

    def __init__(
        self, project: Project, schema: DataSchema, name: str = "unnamed dataset"
    ) -> None:
        super().__init__()
        self._schema = schema
        self._project = project
        self._name = name

    @property
    def project(self):
        return self._project

    @property
    def roles(self):
        return Roles(self)

    @property
    def name(self) -> str:
        return self._name

    @abc.abstractproperty
    def hash(self) -> Optional[bytes]:
        pass

    @abc.abstractmethod
    def datapoint(self, index: Any) -> Datapoint:
        pass

    @abc.abstractproperty
    def columns(self) -> Iterable[str]:
        pass

    @abc.abstractproperty
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

    @abc.abstractproperty
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
