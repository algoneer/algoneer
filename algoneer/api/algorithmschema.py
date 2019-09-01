from .object import Object
from .manager import Manager
from algoneer.algorithm import AlgorithmAlgorithmSchema as AAlgorithmSchema

from typing import Dict, Any, Optional


class AlgorithmSchema(Object):
    Type = AAlgorithmSchema

    @property
    def dependencies(self):
        return []

    @property
    def data(self) -> Dict[str, Any]:
        return self.mapped_obj.schema.dump()


class AlgorithmSchemas(Manager[AlgorithmSchema]):
    Type = AlgorithmSchema

    def url(self, obj: AlgorithmSchema) -> str:
        algo = self.session.get_saved(obj.mapped_obj.algorithm)
        return "/algorithms/{}/schemas".format(algo.id)
        return ""
