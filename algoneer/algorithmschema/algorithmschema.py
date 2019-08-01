from enum import Enum

from typing import Mapping, Any, Optional


class AlgorithmSchema:

    """An AlgorithmSchema contains information about a given algorithm that
    Algoneer can use to determine e.g. which tests can be run on it.
    """

    class Type(Enum):

        Classifier = 1
        Regressor = 2
        Cluster = 3
        Transformer = 4

    def __init__(self, type: Type, config: Optional[Mapping[str, Any]] = None) -> None:
        self._type = type
        if config is None:
            config = {}
        self._config = config

    @property
    def config(self) -> Mapping[str, Any]:
        return self._config

    @property
    def type(self) -> Type:
        return self._type
