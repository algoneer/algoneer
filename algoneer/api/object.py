from typing import Dict, Any, Optional, TypeVar, Generic, Type

from algoneer import Object as AObject
import algoneer.api

import abc


T = TypeVar("T", bound=AObject)


class Object(abc.ABC, Generic[T]):
    """
    All API objects inherit from this class.
    """

    Type: Type[T]

    def __init__(
        self,
        data: Dict[str, Any],
        session: Optional["algoneer.api.Session"] = None,
        object: Optional[AObject] = None,
    ):
        self._object = object
        self._data = data
        self._session = session

    @property
    def object(self) -> Optional[AObject]:
        return self._object

    @property
    def session(self) -> Optional["algoneer.api.Session"]:
        return self._session

    @property
    def data(self) -> Dict[str, Any]:
        return self._data

    @data.setter
    def data(self, data: Dict[str, Any]) -> None:
        self._data = data

    @property
    def id(self) -> Optional[str]:
        return self._data.get("id")

    @id.setter
    def id(self, id: Optional[str]) -> None:
        self._data["id"] = id
