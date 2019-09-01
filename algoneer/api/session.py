from typing import List, Optional, Dict, Type, Set
from .base_client import BaseClient
from .object import Object as Object, get_class_for
from .manager import Manager, get_manager_for
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
        Adds a given object to the} session and returns the corresponding API
        oject.
        """
        if obj in self._obj_map:
            return self._obj_map[obj]
        MappedClass = get_class_for(type(obj))
        if MappedClass is None:
            raise ValueError(
                "no mapping for object of type '{}'".format(type(obj).__name__)
            )
        mapped_obj = MappedClass(obj=obj, session=self)
        self._inv_obj_map[mapped_obj] = obj
        self._obj_map[obj] = mapped_obj
        return mapped_obj

    def __getitem__(self, obj: AObject) -> Optional[Object]:
        return self._obj_map.get(obj)

    def sync(self) -> None:
        """
        Synchronizes all objs present in the session with the backend.
        
        * For each object in the session:
          * Get dependent objects and insert them before the object
          * Save the object using its query manager (which extracts the relevant
            data and the ID and queries the API)
        """
        managers: Dict[Type[Object], Manager] = {}
        objs_to_add: List[Object] = []
        objs: Set[Object] = set()

        def add_obj(obj: Object):
            dependencies = obj.dependencies
            for dependency in dependencies:
                dep = self.add(dependency)
                add_obj(dep)
            if not obj in objs:
                objs_to_add.append(obj)
                objs.add(obj)

        for obj in list(self._obj_map.values()):
            add_obj(obj)
        for obj in objs_to_add:
            if not type(obj) in managers:
                ManagerClass = get_manager_for(type(obj))
                if ManagerClass is None:
                    raise ValueError(
                        "no manager class defined for type {}".format(
                            type(obj).__name__
                        )
                    )
                managers[type(obj)] = ManagerClass(self)
            manager = managers[type(obj)]
            manager.save(obj)

    def __contains__(self, obj: AObject) -> bool:
        return obj in self._obj_map
