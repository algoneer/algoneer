from .object import Object
from .manager import Manager
from algoneer.algorithm import Algorithm as AAlgorithm

from typing import Dict, Any, Optional


class Algorithm(Object):
    Type = AAlgorithm

    @property
    def dependencies(self):
        return [self.mapped_obj.project]

    @property
    def dependants(self):
        return [self.mapped_obj.algorithm_schema]


class Algorithms(Manager[Algorithm]):
    Type = Algorithm

    def url(self, obj: Algorithm) -> str:
        if obj.id is None:
            project = self.session.get_saved(obj.mapped_obj.project)
            return "projects/{}/algorithms".format(project.id)
        return "algorithms/{}".format(obj.id)
