from typing import Dict, Any, Optional


class Object:
    """
    All API objects inherit from this class.
    """

    def __init__(self, data: Dict[str, Any]) -> None:
        self._data = data

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
