from typing import Type, List, TypeVar, Generic
from .object import Object
import algoneer.api
import json
import abc

from typing import TypeVar, Generic, Dict, Any, Optional

T = TypeVar("T", bound=Object)

import datetime
import base64


class Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            if obj.utcoffset() is not None:
                raise ValueError("Expected a UTC datetime!")
            return obj.strftime("%Y-%m-%dT%H:%M:%SZ")
        elif isinstance(obj, (bytes, bytearray)):
            return base64.b64encode(obj).decode("ascii")
        return json.JSONEncoder.default(self, obj)


class ManagerMeta(abc.ABCMeta):
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

    @abc.abstractmethod
    def url(self, obj: T) -> str:
        """
        Returns the URL to create/update an object
        """
        raise NotImplementedError

    def __init__(self, session: "algoneer.api.Session") -> None:
        self.session = session

    def save(self, obj: T) -> bool:
        if obj.id is not None:
            return self._update(obj)
        return self._create(obj)

    def _create(self, obj: T) -> bool:
        """
        Create a new object.
        """
        url = self.url(obj)
        response = self.session.client.post(
            url,
            data=json.dumps(obj.data, cls=Encoder),
            headers={"Content-Type": "application/json"},
        )
        if response.status_code != 201:
            raise IOError()
        assert response.data is not None
        obj.api_data = response.data
        return True

    def _update(self, obj: T) -> bool:
        """
        Update an existing object.
        """
        assert obj.id is not None
        url = self.url(obj)
        response = self.session.client.patch(url, data=obj.data)
        if response.status_code != 200:
            raise IOError()
        assert response.data is not None
        obj.api_data = response.data
        return True


mappings: Dict[Type[Object], Type[Manager]] = {}


def get_manager_for(cls: Type[Object]) -> Optional[Type[Manager]]:
    for potential_cls in [cls] + list(cls.__bases__):
        if potential_cls in mappings:
            return mappings[potential_cls]
    return None
