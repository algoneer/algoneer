import algoneer
import abc

from typing import Dict, Any, Optional


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

    @abc.abstractproperty
    def hash(self) -> Optional[bytes]:
        pass

    @property
    @abc.abstractmethod
    def index(self) -> Any:
        pass

    @property
    @abc.abstractmethod
    def data(self) -> Dict[str, Any]:
        pass
