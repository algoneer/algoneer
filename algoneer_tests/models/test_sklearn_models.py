from algoneer_datasets.bike_sharing import load_dataset
from algoneer.algorithm import Algorithm
from algoneer.model import Model
from algoneer.project import Project

import unittest

try:
    import sklearn
    test = True
except ModuleNotFoundError:
    test = False

class SklearnModelTest(unittest.TestCase):

    @unittest.skipIf(not test, "sklearn module not available")
    def test_sklean(self):

        from algoneer.algorithm.sklearn import SklearnAlgorithm
        from sklearn.ensemble import RandomForestRegressor

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)

        algo = SklearnAlgorithm(project, RandomForestRegressor, n_estimators=100)

        assert isinstance(algo, Algorithm)

        assert 'kwargs' in algo.data and algo.data['kwargs'] == {"n_estimators" : 100, "random_state" : 0}

        model = algo.fit(dataset)

        assert isinstance(model, Model)
