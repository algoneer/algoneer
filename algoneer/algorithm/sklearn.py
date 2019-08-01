from .algorithm import Algorithm

import sklearn

from algoneer.algorithmschema import AlgorithmSchema
from algoneer.dataset.pandas import PandasDataSet
from algoneer.dataset import DataSet

from algoneer.model.sklearn import SklearnModel
from algoneer.model import Model
import sklearn.base as base  # type: ignore

from typing import Optional


class SklearnAlgorithm(Algorithm):
    def __init__(self, estimator: sklearn.base.BaseEstimator):
        self._estimator = estimator

        schema: Optional[AlgorithmSchema] = None
        if isinstance(estimator, base.ClassifierMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Classifier)
        elif isinstance(estimator, base.RegressorMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Regressor)
        elif isinstance(estimator, base.ClusterMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Cluster)

        super().__init__(schema=schema)

    def fit(self, dataset: DataSet) -> Model:
        """
        Fits a dataset to the estimator. To do this, we convert the dataset
        into a pandas dataframe first.
        """

        pd_dataset = PandasDataSet.from_dataset(dataset)

        # we get the attributes that have the "x" role assigned to them
        x = pd_dataset.roles.x

        # we get the attributes that have the "y" role assigned to them
        y = pd_dataset.roles.y

        # we clone the estimator to not overwrite it
        estimator = sklearn.base.clone(self._estimator)

        # we fit the estimator with the x and y dataframes
        estimator.fit(x.df, y.df)

        return SklearnModel(self, estimator)
