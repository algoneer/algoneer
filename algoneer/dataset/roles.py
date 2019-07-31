import algoneer

from typing import List


class Roles:
    def __init__(self, dataset: "algoneer.DataSet") -> None:
        d = self.__dict__
        d["_dataset"] = dataset

    def __getattr__(self, role: str) -> "algoneer.DataSet":
        """
        We return a dataset with all attributes that have the given role
        """
        relevant_columns: List[str] = []
        for key, attribute in self._dataset.attributes.items():
            if role in attribute.roles:
                relevant_columns.append(attribute.column)
        return self._dataset[relevant_columns]
