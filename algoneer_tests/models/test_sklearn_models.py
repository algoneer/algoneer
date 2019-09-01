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

        # we ensure that we always obtain the same result when training the model with the same data
        assert model.hash ==b'\x01\x00\x00\x00\x87\x7f\xe4o\xbd\xbeD\xc1r\xf4+3\x89\xb6\xf5{U\xfd\x06\xe6\xe6\x11\xfe\xc3\x1c\x91+\xb9\x84EH\xae'
