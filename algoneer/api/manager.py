from typing import Type, List, TypeVar, Generic
from .object import Object
import algoneer.api

from typing import TypeVar, Generic, Dict, Any, Optional

T = TypeVar("T", bound=Object)


class ManagerMeta(type):
    def __init__(cls, name: str, bases, namespace) -> None:
        """
        We add the mapped class to the mappings dictionary, which allows the
        session to determine the correct API object for a given Algoneer object.
        """
        if hasattr(cls, "Type"):
            mappings[cls.Type] = cls  # type: ignore
        super().__init__(name, bases, namespace)


class Manager(Generic[T], metaclass=ManagerMeta):

    Type: Type[T]
    url: str = ""

    def object_url(self, id: str) -> str:
        """
        Returns the URL for a specific object
        """
        return self.url.format(id=id)

    def list_url(self) -> str:
        """
        Returns the URL to list objects
        """
        return self.url

    def create_url(self) -> str:
        """
        Returns the URL to create an object
        """
        return self.url

    def create_obj(self, data: Dict[str, Any]) -> T:
        return self.Type(data=data, session=self.session)

    def __init__(self, session: "algoneer.api.Session") -> None:
        self.session = session

    def list(self, params: Optional[Dict[str, Any]] = None) -> List[T]:
        """
        List all objects of a given type.
        """
        url = self.list_url()
        response = self.session.client.get(url, params=params)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        objs: List[T] = []
        for obj_data in response.data["data"]:
            objs.append(self.create_obj(obj_data))
        return objs

    def get(self, id: str, params: Optional[Dict[str, Any]] = None) -> T:
        """
        Get an object by its ID.
        """
        url = self.object_url(id)
        response = self.session.client.get(url, params=params)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        return self.create_obj(response.data)

    def save(self, obj: T) -> bool:
        if obj.id is not None:
            return self._update(obj)
        return self._create(obj)

    def _create(self, obj: T) -> bool:
        """
        Create a new object.
        """
        url = self.create_url()
        response = self.session.client.post(url, data=obj.data)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        obj.data = response.data
        return True

    def _update(self, obj: T) -> bool:
        """
        Update an existing object.
        """
        assert obj.id is not None
        url = self.object_url(obj.id)
        response = self.session.client.patch(url, data=obj.data)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        obj.data = response.data
        return True

    def delete(self, obj: T) -> bool:
        """
        Delete an existing ovject.
        """
        assert obj.id is not None
        url = self.object_url(obj.id)
        response = self.session.client.delete(url)
        if response.status_code != 200:
            raise IOError
        obj.id = None
        return True


mappings: Dict[Type[Object], Type[Manager]] = {}


def get_manager_for(cls: Type[Object]) -> Optional[Type[Manager]]:
    for potential_cls in [cls] + list(cls.__bases__):
        if potential_cls in mappings:
            return mappings[potential_cls]
    return None
