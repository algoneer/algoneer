from .result import Result, ResultProxy
from algoneer.model import Model
from algoneer.model import Model
from algoneer.object import Object


class ModelResult(Object, ResultProxy):
    def __init__(self, model: Model, result: Result):
        Object.__init__(self)
        ResultProxy.__init__(self, result)
        self._model = model
