from .algorithm import Algorithm

import sklearn

from algoneer.dataset.pandas import PandasDataSet
from algoneer.dataset import DataSet

from algoneer.model.sklearn import SklearnModel
from algoneer.model import Model

class SklearnAlgorithm(Algorithm):
    
    def __init__(self, estimator: sklearn.base.BaseEstimator):
        self._estimator = estimator

    def fit(self, dataset : DataSet) -> Model:
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

        return SklearnModel(estimator)