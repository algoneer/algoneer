import abc

import algoneer.model
from algoneer.dataset import DataSet
from algoneer.algorithmschema import AlgorithmSchema

from typing import Optional


class Algorithm(abc.ABC):
    def __init__(self, schema: Optional[AlgorithmSchema] = None) -> None:
        self._schema = schema

    def __getattr__(self, attr):
        if attr.startswith("is_"):
            _type = attr[3:]
            if self.schema is not None and self.schema.type.name.lower() == _type:
                return True
            return False
        return super().__getattr__(attr)

    @property  # type: ignore
    def schema(self) -> Optional[AlgorithmSchema]:
        return self._schema

    @schema.setter  # type: ignore
    def schema(self, schema: Optional[AlgorithmSchema]) -> None:
        self.schema = schema

    @abc.abstractmethod
    def fit(self, data: DataSet) -> "algoneer.model.Model":
        pass
