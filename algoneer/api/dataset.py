from .object import Object
from .manager import Manager
from algoneer.dataset import Dataset as ADataset

from typing import Dict, Any, Optional


class Dataset(Object):
    Type = ADataset

    @property
    def dependencies(self):
        return [self.mapped_obj.project]

    @property
    def dependants(self):
        return [self.mapped_obj.dataschema]


class Datasets(Manager[Dataset]):
    Type = Dataset

    def url(self, obj: Dataset) -> str:
        if obj.id is None:
            project = self.session.get_saved(obj.mapped_obj.project)
            return "projects/{}/datasets".format(project.id)
        return "datasets/{}".format(obj.id)
