from .object import Object
from .manager import Manager
from algoneer.project import Project as AProject
from algoneer.object import Object as AObject

from typing import Dict, Any, Optional, List


class Project(Object):
    Type = AProject

    @property
    def data(self) -> Dict[str, Any]:
        return {}

    @property
    def dependencies(self) -> List[AObject]:
        return []


class Projects(Manager[Project]):
    Type = Project

    def url(self, obj: Optional[Project]) -> str:
        return ""
