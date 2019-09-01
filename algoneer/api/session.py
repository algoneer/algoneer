from typing import List, Optional, Dict, Type
from .base_client import BaseClient
from .object import Object as Object, get_class_for
from algoneer.object import Object as AObject


class Session:
    def __init__(
        self, client: BaseClient, exclude_classes: Optional[List[str]] = ["datapoint"]
    ):
        self._client = client
        self._exclude_classes = exclude_classes
        self._obj_map: Dict[AObject, Object] = {}
        self._inv_obj_map: Dict[Object, AObject] = {}

    @property
    def client(self):
        return self._client

    def add(self, obj: AObject) -> Object:
        """
        Adds a given object to the session and returns the corresponding API
        oject.
        """
        MappedClass = get_class_for(type(obj))
        if MappedClass is None:
            raise ValueError("no mapping for object")
        mapped_obj = MappedClass(obj=obj, session=self)
        self._inv_obj_map[mapped_obj] = obj
        self._obj_map[obj] = mapped_obj
        return mapped_obj

    def __getitem__(self, obj: AObject) -> Optional[Object]:
        return self._obj_map.get(obj)

    def sync(self) -> None:
        """
        Synchronizes all objs present in the session with the backend.

        * Sort all session objs by their dependencies.
        * For each obj, retrieve the backend URL for storing it.
        * Call the API to create or update the obj and retrieve its ID.
        * Store the ID and data in the API obj class.
        * Done :)
        """
        pass

    def __contains__(self, obj: AObject) -> bool:
        return obj in self._obj_map
