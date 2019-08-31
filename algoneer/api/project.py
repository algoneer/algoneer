from .object import Object
from .objects import Objects


class Project(Object):
    pass


class Projects(Objects[Project]):
    Type = Project
