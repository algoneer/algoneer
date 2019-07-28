from algoneer.dataschema import DataSchema
import abc

class DataSet(abc.ABC):

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
    """

    @abc.abstractmethod
    def enforce_schema(self, schema: DataSchema) -> None:
        pass
    
    @staticmethod
    @abc.abstractmethod
    def from_path(path: str) -> 'DataSet':
        pass