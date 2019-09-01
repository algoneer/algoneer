from typing import List, Optional, Dict, Type
from .base_client import BaseClient
from .object import Object as AObject
from algoneer.object import Object


class Session:
    def __init__(
        self, client: BaseClient, exclude_classes: Optional[List[str]] = ["datapoint"]
    ):
        self._client = client
        self._exclude_classes = exclude_classes
        self._objects: Dict[int, AObject] = {}

    @property
    def client(self):
        return self._client

    def add(self, object: AObject) -> None:
        self._objects[id(object)] = object

    def get_api_object(self, object: AObject) -> Optional[Object]:
        pass

    def sync(self) -> None:
        """
        Synchronizes all objects present in the session with the backend.

        * Sort all session objects by their dependencies.
        * For each object, retrieve the backend URL for storing it.
        * Call the API to create or update the object and retrieve its ID.
        * Store the ID and data in the API object class.
        * Done :)
        """
        pass

    def __contains__(self, object: AObject) -> bool:
        return id(object) in self._objects
