from .object import Object

from typing import Dict, Any


class Project(Object):
    def __init__(self, path: str) -> None:
        super().__init__()
        self._path = path

    @property
    def path(self):
        return self._path

    def dump(self) -> Dict[str, Any]:
        return {"path": self._path}

    def load(self, data: Dict[str, Any]) -> None:
        pass
