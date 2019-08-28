import algoneer
import abc

from typing import Dict, Any


class Datapoint(abc.ABC):

    """Describes a single datapoint.
    """

    @property
    @abc.abstractmethod
    def dataset(self) -> "algoneer.Dataset":
        pass

    @abc.abstractmethod
    def copy(self) -> "Datapoint":
        pass

    @property
    @abc.abstractmethod
    def data(self) -> Dict[str, Any]:
        pass
