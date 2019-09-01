from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms

from algoneer.result import DatasetModelResult
from algoneer.project import Project

import unittest
import math

try:
    import shap
    test_shap = True
except ModuleNotFoundError:
    test_shap = False

class SHAPTest(unittest.TestCase):

    @unittest.skipIf(not test_shap, "SHAP module not available")
    def test_shap(self) -> None:

        from algoneer.methods.blackbox.shap import SHAP, SHAPDatapointResult, SHAPModelResult

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm(project, 'linear-regression')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        # we initialize a SHAP test
        shap = SHAP()

        # we run the SHAP test on the model and dataset
        result = shap.run(dataset, model, max_datapoints=10)

        # we make sure that we obtain a reasonable result
        assert isinstance(result, DatasetModelResult)

        assert 'expected_value' in result.data
        assert math.fabs(result.data['expected_value'] - 1564.6577928309937) < 1e-7