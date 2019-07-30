from . import DataSet

from typing import Optional

from ..dataschema import AttributeSchema

import abc

class Attribute(abc.ABC):

    @abc.abstractmethod
    def __init__(self, dataset: DataSet, column : str, schema : Optional[AttributeSchema]) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def column(self) -> str:
        pass

    @column.setter # type: ignore
    @abc.abstractmethod
    def column(self, column : str) -> None:
        pass

    @property # type: ignore
    @abc.abstractmethod
    def schema(self) -> Optional[AttributeSchema]:
        pass

    @schema.setter # type: ignore
    @abc.abstractmethod
    def schema(self, schema : Optional[AttributeSchema]) -> None:
        pass