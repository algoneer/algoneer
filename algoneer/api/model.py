from .object import Object
from .manager import Manager
from algoneer.model.model import Model as AModel

from typing import Dict, Any, Optional


class Model(Object):
    Type = AModel

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Models(Manager[Model]):
    Type = Model

    def url(self, obj: Optional[Model]) -> str:
        return ""
