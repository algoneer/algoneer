import abc
from typing import Optional, Dict, Any


class Object(abc.ABC):
    @abc.abstractmethod
    def dump(self) -> Dict[str, Any]:
        raise NotImplementedError

    @abc.abstractmethod
    def load(self, data: Dict[str, Any]) -> None:
        raise NotImplementedError
