import abc

import algoneer.api.session
from .response import Response


class BaseClient(abc.ABC):
    @abc.abstractmethod
    def get(self, url: str, **kwargs) -> Response:
        pass

    @abc.abstractmethod
    def post(self, url: str, **kwargs) -> Response:
        pass

    @abc.abstractmethod
    def patch(self, url: str, **kwargs) -> Response:
        pass

    @abc.abstractmethod
    def delete(self, url: str, **kwargs) -> Response:
        pass

    def session(self) -> "algoneer.api.session.Session":
        return algoneer.api.session.Session(self)
