from .object import Object
from .manager import Manager
from algoneer.dataset import DatasetDataSchema as ADataSchema

from typing import Dict, Any, Optional


class DataSchema(Object):
    Type = ADataSchema

    @property
    def dependencies(self):
        return []

    @property
    def data(self) -> Dict[str, Any]:
        return self.mapped_obj.schema.dump()


class DataSchemas(Manager[DataSchema]):
    Type = DataSchema

    def url(self, obj: DataSchema) -> str:
        dataset = self.session.get_saved(obj.mapped_obj.dataset)
        return "/datasets/{}/schemas".format(dataset.id)
        return ""
