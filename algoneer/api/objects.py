from typing import Type, List, TypeVar, Generic
from .object import Object
from .session import Session
import abc

from typing import TypeVar, Generic, Dict, Any, Optional

T = TypeVar("T", bound=Object)


class Objects(abc.ABC, Generic[T]):

    Type: Type[T]

    @abc.abstractmethod
    def object_url(self, id: str) -> str:
        """
        Returns the URL for a specific object
        """

    @abc.abstractmethod
    def list_url(self) -> str:
        """
        Returns the URL to list objects
        """

    @abc.abstractmethod
    def create_url(self) -> str:
        """
        Returns the URL to create an object
        """

    def create_obj(self, data: Dict[str, Any]) -> T:
        return self.Type(data=data, session=self.session)

    def __init__(self, session: Session) -> None:
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
        return self.Type(response.data)

    def create(self, obj: T) -> bool:
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

    def update(self, obj: T) -> bool:
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
