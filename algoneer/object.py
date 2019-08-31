from algoneer.api import APIObject

from typing import Optional


class Object:
    def __init__(self) -> None:
        self._api_object: Optional[APIObject] = None

    @property
    def api_object(self) -> Optional[APIObject]:
        return self._api_object

    @api_object.setter
    def api_object(self, obj: Optional[APIObject]) -> None:
        self._api_object = obj
