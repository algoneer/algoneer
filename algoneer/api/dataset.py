from .object import Object
from .manager import Manager
from algoneer.dataset import Dataset as ADataset

from typing import Dict, Any


class Dataset(Object):
    Type = ADataset

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Datasets(Manager[Dataset]):
    Type = Dataset
