from .object import Object
from .manager import Manager
from algoneer.model.model import Model as AModel

from typing import Dict, Any


class Model(Object):
    Type = AModel

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Models(Manager[Model]):
    Type = Model
