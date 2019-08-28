import algoneer

from typing import List, Union


class Roles:
    def __init__(self, obj: "algoneer.dataset.Dataset") -> None:
        d = self.__dict__
        d["_obj"] = obj

    def __getattr__(
        self, role: str
    ) -> Union["algoneer.dataset.Dataset", "algoneer.dataset.Attribute"]:
        """
        We return a dataset or datapoint with all attributes that have the given role
        """
        relevant_columns: List[str] = []
        for attribute in self._obj.attributes.values():
            if role in attribute.roles:
                relevant_columns.append(attribute.column)
        return self._obj[relevant_columns]
