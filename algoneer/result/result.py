import abc

from typing import Dict, Any


class Result(abc.ABC):
    @property
    @abc.abstractmethod
    def data(self) -> Dict[str, Any]:
        pass

    @abc.abstractmethod
    def format(self, format: str) -> Any:
        pass
