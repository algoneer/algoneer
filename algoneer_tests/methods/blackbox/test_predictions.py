from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.predictions import Predictions, PredictionsResult

from algoneer.result import DatasetModelResult
from algoneer.project import Project

import unittest

class TestPredictions(unittest.TestCase):

    def test_predictions(self) -> None:

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm(project, 'random-forest')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        # we initialize a predictions test
        predictions = Predictions()

        # we run the predictions test on the model and dataset
        result = predictions.run(dataset, model, max_datapoints=110)

        # we make sure that we obtain a reasonable result
        assert isinstance(result, DatasetModelResult)