from .object import Object


class Project(Object):
    def __init__(self, name: str) -> None:
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name
