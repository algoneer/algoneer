from enum import Enum

from typing import Mapping, Iterable, Any

import algoneer.dataschema
import algoneer.dataset


class AttributeSchema:
    class Type(Enum):

        Numerical = 1
        Timestamp = 2
        Integer = 3
        Float = 4
        Ordinal = 5
        Categorical = 6
        Unknown = 7

    def __init__(
        self,
        ds: "algoneer.dataschema.DataSchema",
        column: str,
        roles: Iterable[str],
        type: Type,
        config: Mapping[str, Any],
    ) -> None:
        self._ds = ds
        self._type = type
        self._column = column
        self._roles = roles
        self._config = config

    @property
    def config(self):
        return self._config

    @property
    def type(self):
        return self._type

    @property
    def roles(self):
        return self._roles

    @property
    def column(self):
        return self._column

    def enforce(self, ds: "algoneer.dataset.DataSet"):
        attribute = ds[self.column]
        assert isinstance(attribute, algoneer.dataset.Attribute)
        # we can test our luck...
        ds[self.column] = attribute.astype(self._type, config=self.config)
