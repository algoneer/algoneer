from .algorithm import Algorithm

import sklearn
import platform

from algoneer.algorithmschema import AlgorithmSchema
from algoneer.dataset.pandas import PandasDataset
from algoneer.dataset import Dataset

from algoneer.model.sklearn import SklearnModel
from algoneer.model import Model
from algoneer.project import Project

from typing import Optional, Mapping, Any, Type, Dict


class SklearnAlgorithm(Algorithm):
    def __init__(
        self,
        project: Project,
        estimator_class: Type[sklearn.base.BaseEstimator],
        **kwargs
    ):

        if kwargs is None:
            kwargs = {}

        self._estimator_class = estimator_class
        self._kwargs = kwargs.copy()

        if not "random_state" in self._kwargs:
            self._kwargs["random_state"] = 0

        if issubclass(estimator_class, sklearn.base.ClassifierMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Classifier)
        elif issubclass(estimator_class, sklearn.base.RegressorMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Regressor)
        elif issubclass(estimator_class, sklearn.base.ClusterMixin):
            schema = AlgorithmSchema(type=AlgorithmSchema.Type.Cluster)

        super().__init__(project=project, schema=schema)

    @property
    def name(self) -> str:
        return self._estimator_class.__name__

    @property
    def data(self) -> Dict[str, Any]:
        return {
            "kwargs": self._kwargs,
            "version": sklearn.__version__,
            "platform": {
                "machine": platform.machine(),
                "python": platform.python_version(),
            },
        }

    def fit(self, dataset: Dataset) -> Model:
        """
        Fits a dataset to the estimator. To do this, we convert the dataset
        into a pandas dataframe first.
        """

        pd_dataset = PandasDataset.from_dataset(dataset)

        # we get the attributes that have the "x" role assigned to them
        x = pd_dataset.roles.x

        # we get the attributes that have the "y" role assigned to them
        y = pd_dataset.roles.y

        if y.shape[1] != 1:
            raise ValueError("more than one y attribute found")

        # we convert the dataset to an attribute
        y = y[y.columns[0]]

        kwargs = self._kwargs.copy()

        try:
            # we create a new estimator with the given arguments
            estimator = self._estimator_class(**kwargs)
        except:
            # we delete the random_state argument, as it might not be supported by all estimators
            del kwargs["random_state"]
            estimator = self._estimator_class(**kwargs)

        # we fit the estimator with the x and y dataframes
        estimator.fit(x.df, y.series)

        return SklearnModel(self, dataset, estimator)
