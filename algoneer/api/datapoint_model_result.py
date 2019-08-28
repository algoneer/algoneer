from .object import APIObject
from .objects import APIObjects


class APIDatapointModelResult(APIObject):
    pass


class APIDatapointModelResults(APIObjects[APIDatapointModelResult]):
    Type = APIDatapointModelResult
