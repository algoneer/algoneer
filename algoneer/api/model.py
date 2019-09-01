from .object import Object
from .manager import Manager
from algoneer.model.model import Model as AModel

from typing import Dict, Any, Optional


class Model(Object):
    Type = AModel

    @property
    def dependencies(self):
        return [self.mapped_obj.algorithm, self.mapped_obj.dataset]


class Models(Manager[Model]):
    Type = Model

    def url(self, obj: Model) -> str:
        if obj.id is None:
            algo = self.session.get_saved(obj.mapped_obj.algorithm)
            dataset = self.session.get_saved(obj.mapped_obj.dataset)
            return "/dataset/{}/algorithms/{}/models".format(dataset.id, algo.id)
        return "/projects/{}".format(obj.id)
