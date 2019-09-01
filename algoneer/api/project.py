from .object import Object
from .manager import Manager
from algoneer.project import Project as AProject


class Project(Object):
    Type = AProject


class Projects(Manager[Project]):
    Type = Project
