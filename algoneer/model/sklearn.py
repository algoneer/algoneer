from .model import Model

import pandas as pd
import sklearn

from algoneer.dataset.pandas import PandasDataset
from algoneer.dataset import Dataset
from algoneer.algorithm import Algorithm

from typing import Any, Union


class SklearnModel(Model):
    def __init__(self, algorithm: Algorithm, estimator: sklearn.base.BaseEstimator):
        super().__init__(algorithm=algorithm)
        self._estimator = estimator

    def _predict_raw(self, dataset: Any) -> Any:
        """
        Directly calls the `predict` method of the underlying estimator with an
        arbitrary argument and returns the result without wrapping it into a
        dataset. This is useful for interoperability with 
        """
        return self._estimator.predict(dataset)

    def predict(self, dataset: Union[Dataset, Any]) -> Dataset:

        if not isinstance(dataset, Dataset):
            # if we don't get a dataset we return the raw value
            return self._predict_raw(dataset)

        pd_dataset = PandasDataset.from_dataset(dataset)

        # we get the attributes that have the "x" role assigned to them
        x = pd_dataset.roles.x

        columns = list(dataset.roles.y.schema.attributes.keys())

        # we predict the value using an sklearn estimator
        y = pd.DataFrame(self._estimator.predict(x.df), columns=columns)

        # we return a new dataset and return it
        return PandasDataset(dataset.roles.y.schema, y)
