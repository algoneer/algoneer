from enum import Enum

from typing import Mapping, Any


class AlgorithmSchema:

    """An AlgorithmSchema contains information about a given algorithm that
    Algoneer can use to determine e.g. which tests can be run on it.
    """

    class Type(Enum):

        Classification = 1
        Regression = 2
        Clustering = 3

    def __init__(self, type: Type, config: Mapping[str, Any]) -> None:
        self._type = type
        self._config = config

    @property
    def config(self) -> Mapping[str, Any]:
        return self._config

    @property
    def type(self) -> Type:
        return self._type
