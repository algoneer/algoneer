from enum import Enum

from typing import Mapping, Any

import algoneer.dataschema as dataschema


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
        ds: "dataschema.DataSchema",
        column: str,
        type: Type,
        config: Mapping[str, Any],
    ) -> None:
        self._ds = ds
        self._type = type
        self._column = column
        self._config = config
