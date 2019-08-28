from .object import APIObject
from .objects import APIObjects


class APIDatapoint(APIObject):
    pass


class APIDatapoints(APIObjects[APIDatapoint]):
    Type = APIDatapoint
