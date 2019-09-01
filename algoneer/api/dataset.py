from .object import Object
from .manager import Manager
from algoneer.dataset import Dataset as ADataset


class Dataset(Object):
    Type = ADataset


class Datasets(Manager[Dataset]):
    Type = Dataset
