from typing import List, Optional
from .base_client import BaseClient
from algoneer.object import Object

class Session:
    def __init__(
        self, client: BaseClient, exclude_classes: Optional[List[str]] = ["datapoint"]
    ):
        self._client = client
        self._exclude_classes = exclude_classes
        self._objects = {}

    def add(self, object: Object) -> None:
        self._objects[id(object)] = object

    def sync(self) -> None:
        pass

    def __contains__(self, object: Object) -> bool:
        return id(object) in self._objects