import abc

from algoneer.model import Model
from algoneer.dataset import DataSet

class Algorithm(abc.ABC):
    
    @abc.abstractmethod
    def fit(self, data : DataSet) -> Model:
        pass

