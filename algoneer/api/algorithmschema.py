from .object import Object
from .manager import Manager
from algoneer.algorithmschema import AlgorithmSchema as AAlgorithmSchema

from typing import Dict, Any, Optional


class AlgorithmSchema(Object):
    Type = AAlgorithmSchema

    @property
    def dependencies(self):
        return []


class AlgorithmSchemas(Manager[AlgorithmSchema]):
    Type = AlgorithmSchema

    def url(self, obj: Optional[AlgorithmSchema]) -> str:
        return ""
