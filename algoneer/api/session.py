from typing import List, Optional


class APISession:
    def __init__(self, exclude_classes: Optional[List[str]] = ["datapoint"]):
        self._exclude_classes = exclude_classes
