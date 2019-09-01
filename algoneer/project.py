from .object import Object

from typing import Dict, Any


class Project(Object):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def dump(self) -> Dict[str, Any]:
        return {}

    def load(self, data: Dict[str, Any]) -> None:
        pass
