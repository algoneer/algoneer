from .object import Object
from .manager import Manager
from algoneer.project import Project as AProject

from typing import Dict, Any


class Project(Object):
    Type = AProject

    @property
    def data(self) -> Dict[str, Any]:
        return {}


class Projects(Manager[Project]):
    Type = Project
