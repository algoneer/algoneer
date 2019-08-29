from typing import Type, List
from .object import Object
from .client import Client
import abc


class Objects(abc.ABC):

    Type: Type[Object]
    list_url: str
    object_url: str

    def __init__(self, client: Client) -> None:
        self.client = client

    def list(self, **kwargs) -> List[Object]:
        """
        List 
        """
        return []

    def get(self, id: str, **kwargs) -> Object:
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

    def create(self, obj: Object, **kwargs) -> bool:
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

    def update(self, obj: Object, **kwargs) -> bool:
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

    def delete(self, obj: Object, **kwargs) -> bool:
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
