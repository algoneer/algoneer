from .object import Object
from .manager import Manager
from algoneer.algorithmschema import AlgorithmSchema as AAlgorithmSchema

from typing import Dict, Any


class AlgorithmSchema(Object):
    Type = AAlgorithmSchema

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class AlgorithmSchemas(Manager[AlgorithmSchema]):
    Type = AlgorithmSchema
