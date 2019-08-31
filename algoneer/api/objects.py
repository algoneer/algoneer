from typing import Type, List, TypeVar, Generic
from .object import Object
from .client import Client
import abc

from typing import TypeVar, Generic

T = TypeVar("T", bound=Object)


class Objects(abc.ABC, Generic[T]):

    Type: Type[T]
    list_url: str
    object_url: str

    def __init__(self, client: Client) -> None:
        self.client = client

    def list(self, **kwargs) -> List[T]:
        """
        List all objects of a given type.
        """
        return []

    def get(self, id: str, **kwargs) -> T:
        """
        Get an object by its ID.
        """
        args = kwargs.copy()
        args["object_id"] = id
        params = kwargs.get("params", {})
        url = self.object_url.format(**args)
        response = self.client.get(url, params=params)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        return self.Type(response.data)

    def create(self, obj: T, **kwargs) -> bool:
        """
        Create a new object.
        """
        args = kwargs.copy()
        url = self.object_url.format(**args)
        response = self.client.post(url, data=obj.data)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        obj.data = response.data
        return True

    def update(self, obj: T, **kwargs) -> bool:
        """
        Update an existing object.
        """
        args = kwargs.copy()
        args["object_id"] = obj.id
        url = self.object_url.format(**args)
        response = self.client.patch(url, data=obj.data)
        if response.status_code != 200:
            raise IOError
        assert response.data is not None
        obj.data = response.data
        return True

    def delete(self, obj: T, **kwargs) -> bool:
        """
        Delete an existing ovject.
        """
        args = kwargs.copy()
        args["object_id"] = obj.id
        url = self.object_url.format(**args)
        response = self.client.delete(url)
        if response.status_code != 200:
            raise IOError
        obj.id = None
        return True
