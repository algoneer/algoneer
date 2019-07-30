from . import DataSet

from typing import Optional

from ..dataschema import AttributeSchema

import abc

class Attribute(abc.ABC):

    @abc.abstractmethod
    def __init__(self, dataset: DataSet, column : str, schema : Optional[AttributeSchema]) -> None:
        pass

    @abc.abstractmethod # type: ignore
    @property
    def column(self) -> str:
        pass

    @abc.abstractmethod # type: ignore
    @column.setter
    def column(self, column : str) -> None:
        pass

    @abc.abstractmethod # type: ignore
    @property
    def schema(self) -> Optional[AttributeSchema]:
        pass

    @abc.abstractmethod # type: ignore
    @schema.setter
    def schema(self, schema : Optional[AttributeSchema]) -> None:
        pass