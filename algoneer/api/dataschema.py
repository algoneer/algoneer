from .object import Object
from .manager import Manager
from algoneer.dataschema import DataSchema as ADataSchema


class DataSchema(Object):
    Type = ADataSchema


class DataSchemas(Manager[DataSchema]):
    Type = DataSchema
