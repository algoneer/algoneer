from .object import Object
from .manager import Manager
from algoneer.algorithmschema import AlgorithmSchema as AAlgorithmSchema


class AlgorithmSchema(Object):
    Type = AAlgorithmSchema


class AlgorithmSchemas(Manager[AlgorithmSchema]):
    Type = AlgorithmSchema
