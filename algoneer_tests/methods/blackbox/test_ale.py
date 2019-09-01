from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.ale import ALE, ALEResult

from algoneer.result import DatasetModelResult
from algoneer.project import Project

import unittest

class TestALE(unittest.TestCase):

    def test_ale(self) -> None:

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm(project, 'linear-regression')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        # we initialize a ALE test
        ale = ALE()

        columns = ['windspeed', 'hum', 'atemp', 'season']

        # we run the ALE test on the model and dataset
        result = ale.run(dataset, model, columns=columns, max_datapoints=200, n_intervals=10)

        # we make sure that we obtain a reasonable result
        assert isinstance(result, DatasetModelResult)
