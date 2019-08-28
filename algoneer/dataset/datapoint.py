from .dataset import Dataset

import abc


class Datapoint(abc.ABC):

    """Describes a single datapoint.
    """

    @property
    @abc.abstractmethod
    def dataset(self) -> Dataset:
        pass

    @abc.abstractmethod
    def copy(self) -> "Datapoint":
        pass
