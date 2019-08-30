from enum import Enum

from typing import Mapping, Iterable, Any, Optional

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
        Boolean = 7
        Unknown = 8

    def __init__(
        self,
        roles: Iterable[str],
        type: Type,
        ds: Optional["algoneer.dataschema.DataSchema"] = None,
        column: Optional[str] = None,
        config: Optional[Mapping[str, Any]] = None,
    ) -> None:
        if config is None:
            config = {}
        self._ds = ds
        self._type = type
        self._column = column
        self._roles = roles
        self._config = config

    @property
    def dataschema(self):
        return self._ds

    @dataschema.setter
    def dataschema(self, ds):
        self._ds = ds

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

    def copy(self):
        return type(self)(
            roles=self.roles,
            type=self.type,
            ds=self.dataschema,
            column=self.column,
            config=self.config,
        )

    def enforce(self, ds: "algoneer.dataset.Dataset"):
        attribute = ds[self.column]
        assert isinstance(attribute, algoneer.dataset.Attribute)
        # we can test our luck...
        ds[self.column] = attribute.astype(self._type, config=self.config)
