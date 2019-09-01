from .object import Object
from .manager import Manager
from algoneer.dataset import Dataset as ADataset

from typing import Dict, Any, Optional


class Dataset(Object):
    Type = ADataset

    @property
    def data(self) -> Dict[str, Any]:
        return {}

    @property
    def dependencies(self):
        return [self.obj.project]


class Datasets(Manager[Dataset]):
    Type = Dataset

    def url(self, obj: Optional[Dataset]) -> str:
        return ""
