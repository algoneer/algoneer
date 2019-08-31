from typing import List, Optional, Dict, Type
from .base_client import BaseClient

from .algorithm import Algorithm
from .model import Model
from .dataset import Dataset
from .object import Object
from .datapoint_model_result import DatapointModelResult
from .algorithm_result import AlgorithmResult
from .dataset_result import DatasetResult
from .model_result import ModelResult
from .dataschema import DataSchema
from .datapoint import Datapoint
from .algorithmschema import AlgorithmSchema

from algoneer import (
    Object as AObject,
    Model as AModel,
    Algorithm as AAlgorithm,
    AlgorithmSchema as AAlgorithmSchema,
    Dataset as ADataset,
    Datapoint as ADatapoint,
    DataSchema as ADataSchema,
    ModelResult as AModelResult,
    DatasetResult as ADatasetResult,
    AlgorithmResult as AAlgorithmResult,
    DatapointModelResult as ADatapointModelResult,
)

mapping: Dict[Type[AObject], Type[Object]] = {
    AModel: Model,
    AAlgorithm: Algorithm,
    AAlgorithmSchema: AlgorithmSchema,
    ADataset: Dataset,
    ADatapoint: Datapoint,
    ADataset: Dataset,
    ADataSchema: DataSchema,
    ADatapoint: Datapoint,
    AModelResult: ModelResult,
    ADatasetResult: DatasetResult,
    AAlgorithmResult: AlgorithmResult,
    ADatapointModelResult: DatapointModelResult,
}

from typing import Dict, Optional


class Session:
    def __init__(
        self, client: BaseClient, exclude_classes: Optional[List[str]] = ["datapoint"]
    ):
        self._client = client
        self._exclude_classes = exclude_classes
        self._objects: Dict[int, AObject] = {}

    def add(self, object: AObject) -> None:
        self._objects[id(object)] = object

    def get_api_object(self, object: AObject) -> Optional[Object]:
        pass

    def sync(self) -> None:
        """
        Synchronizes all objects present in the session with the backend.
        """
        pass

    def __contains__(self, object: AObject) -> bool:
        return id(object) in self._objects
