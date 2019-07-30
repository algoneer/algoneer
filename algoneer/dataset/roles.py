import abc

import algoneer


class Roles(abc.ABC):
    @abc.abstractmethod
    def __init__(self, dataset: "algoneer.DataSet") -> None:
        pass

    @abc.abstractmethod
    def __getattr__(self, attr) -> "algoneer.DataSet":
        pass
