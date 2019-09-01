from .object import Object
from .objects import Objects
from algoneer.project import Project as AProject


class Project(Object):
    Type = AProject


class Projects(Objects[Project]):
    Type = Project
