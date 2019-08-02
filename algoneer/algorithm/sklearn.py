from .algorithm import Algorithm

import sklearn

from algoneer.algorithmschema import AlgorithmSchema
from algoneer.dataset.pandas import PandasDataSet
from algoneer.dataset import DataSet

from algoneer.model.sklearn import SklearnModel
from algoneer.model import Model

from typing import Optional, Mapping, Any, Type


class SklearnAlgorithm(Algorithm):
    def __init__(
        self,
        estimator_class: Type[sklearn.base.BaseEstimator],
        kwargs: Mapping[str, Any] = None,
    ):

        if kwargs is None:
            kwargs = {}

        self._estimator_class = estimator_class
        self._kwargs = kwargs

        schema: Optional[AlgorithmSchema] = None

        if issubclass(estimator_class, sklearn.base.ClassifierMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Classifier)
        elif issubclass(estimator_class, sklearn.base.RegressorMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Regressor)
        elif issubclass(estimator_class, sklearn.base.ClusterMixin):
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

        if y.shape[1] != 1:
            raise ValueError("more than one y attribute found")

        # we convert the dataset to an attribute
        y = y[y.columns[0]]

        # we create a new estimator with the given arguments
        estimator = self._estimator_class(**self._kwargs)

        # we fit the estimator with the x and y dataframes
        estimator.fit(x.df, y.series)

        return SklearnModel(self, estimator)
