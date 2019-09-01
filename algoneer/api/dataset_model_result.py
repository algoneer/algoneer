from .object import Object
from .manager import Manager
from algoneer.result import DatasetModelResult as ADatasetModelResult

from typing import Dict, Any, Optional


class DatasetModelResult(Object):
    Type = ADatasetModelResult

    @property
    def dependencies(self):
        return [self.mapped_obj.dataset, self.mapped_obj.model]

    @property
    def data(self) -> Dict[str, Any]:
        return self.mapped_obj.result.dump()


class DatasetModelResults(Manager[DatasetModelResult]):

    """
    Stores a dataset model result in the database.
    """

    Type = DatasetModelResult

    def url(self, obj: DatasetModelResult) -> str:
        if obj.id is None:
            model = self.session.get_saved(obj.mapped_obj.model)
            dataset = self.session.get_saved(obj.mapped_obj.dataset)
            return "/dataset/{}/models/{}/results".format(dataset.id, model.id)
        return "/datasets/{}/models/{}/results/{}".format(dataset.id, model.id, obj.id)
