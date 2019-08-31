import abc

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
