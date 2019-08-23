import algoneer.dataset

from typing import Optional, Iterable, Any

from ..dataschema import AttributeSchema

import abc


class Attribute(abc.ABC):
    def __init__(
        self, dataset: "algoneer.dataset.Dataset", column: str, schema: AttributeSchema
    ) -> None:
        self._schema = schema
        self._column = column
        self._dataset = dataset

    def __getattr__(self, attr):
        if attr.startswith("is_"):
            _type = attr[3:]
            if self.schema is not None and self.schema.type.name.lower() == _type:
                return True
            return False
        raise AttributeError("not found")

    @property
    def column(self) -> str:
        return self._column

    @column.setter
    def column(self, column: str) -> None:
        self._column = column

    @property
    def roles(self) -> Iterable[str]:
        return self._schema.roles

    @property
    def schema(self) -> AttributeSchema:
        return self._schema

    @schema.setter
    def schema(self, schema: AttributeSchema) -> None:
        self._schema = schema

    @property
    def dataset(self):
        return self._dataset

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    @abc.abstractmethod
    def sum(self) -> float:
        pass

    @abc.abstractmethod
    def mean(self) -> float:
        pass

    @abc.abstractmethod
    def min(self) -> float:
        pass

    @abc.abstractmethod
    def max(self) -> float:
        pass

    @abc.abstractmethod
    def __getitem__(self, item) -> Any:
        pass
