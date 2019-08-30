class Project:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name
