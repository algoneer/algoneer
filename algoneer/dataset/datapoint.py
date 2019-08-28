from .dataset import Dataset

import abc


class Datapoint(abc.ABC):

    """Describes a single datapoint.
    """

    @abc.abstractmethod
    def hash(self) -> bytes:
        pass

    @property
    @abc.abstractmethod
    def dataset(self) -> Dataset:
        pass

    @abc.abstractmethod
    def copy(self) -> "Datapoint":
        pass
