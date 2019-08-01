from .model import Model

import pandas as pd
import sklearn

from algoneer.dataset.pandas import PandasDataSet
from algoneer.dataset import DataSet, Attribute

from typing import Union


class SklearnModel(Model):
    def __init__(self, estimator: sklearn.base.BaseEstimator):
        self._estimator = estimator

    def predict(self, dataset: DataSet) -> Union[DataSet, Attribute]:

        pd_dataset = PandasDataSet.from_dataset(dataset)

        # we get the attributes that have the "x" role assigned to them
        x = pd_dataset.roles.x

        # we predict the value using an sklearn estimator
        y = pd.DataFrame(self._estimator.predict(x.df))

        return PandasDataSet(y)
