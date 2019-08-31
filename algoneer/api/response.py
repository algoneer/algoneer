from typing import Optional, Any, Dict


class Response:
    def __init__(
        self,
        status_code: int,
        data: Optional[Dict[str, Any]] = None,
        error: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.status_code = status_code
        self.error = error
        self.data = data
