from typing import Optional, Callable, Dict, Any
from .object import Object
from .base_client import BaseClient
from .response import Response
import requests


class Client(BaseClient):
    def __init__(
        self,
        access_token: str,
        base_url: Optional[str] = "https://api.algoneer.org",
        version: Optional[str] = "v1",
    ) -> None:
        self._access_token = access_token
        self._base_url = base_url
        self._version = version

    def _parse_response(self, response: requests.Response) -> Response:
        error: Optional[Dict[str, Any]] = None
        data: Optional[Dict[str, Any]] = {}
        if 200 <= response.status_code < 300:
            data = response.json()
        else:
            error = response.json()
        return Response(response.status_code, data, error)

    def _request(self, method: Callable, url: str, **kwargs) -> Response:
        if not "headers" in kwargs:
            kwargs["headers"] = {}
        headers = kwargs["headers"]
        headers["Authorization"] = f"bearer {self._access_token}"
        full_url = f"{self._base_url}/{self._version}/{url}"
        return self._parse_response(method(url=full_url, **kwargs))

    def get(self, url: str, **kwargs) -> Response:
        return self._request(requests.get, url, **kwargs)

    def post(self, url: str, **kwargs) -> Response:
        return self._request(requests.post, url, **kwargs)

    def patch(self, url: str, **kwargs) -> Response:
        return self._request(requests.get, url, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:
        return self._request(requests.get, url, **kwargs)
