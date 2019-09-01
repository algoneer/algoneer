from .object import Object
from .manager import Manager
from algoneer.project import Project as AProject
from algoneer.object import Object as AObject

from typing import Dict, Any, Optional, List


class Project(Object):
    Type = AProject


class Projects(Manager[Project]):
    Type = Project

    def url(self, obj: Project) -> str:
        if obj.id is not None:
            return "/projects/{}".format(obj.id)
        else:
            return "/organizations/default/project"
