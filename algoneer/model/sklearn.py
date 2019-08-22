from .model import Model

import pandas as pd
import sklearn

from algoneer.dataset.pandas import PandasDataset
from algoneer.dataset import Dataset, Attribute
from algoneer.algorithm import Algorithm

from typing import Union


class SklearnModel(Model):
    def __init__(self, algorithm: Algorithm, estimator: sklearn.base.BaseEstimator):
        super().__init__(algorithm=algorithm)
        self._estimator = estimator

    def predict(self, dataset: Dataset) -> Union[Dataset, Attribute]:

        pd_dataset = PandasDataset.from_dataset(dataset)

        # we get the attributes that have the "x" role assigned to them
        x = pd_dataset.roles.x

        # we predict the value using an sklearn estimator
        y = pd.DataFrame(self._estimator.predict(x.df))

        return PandasDataset(y)
