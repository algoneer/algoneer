from .model import Model

import sklearn


class SklearnModel(Model):
    def __init__(self, estimator: sklearn.base.BaseEstimator):
        self._estimator = estimator
