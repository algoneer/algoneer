from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.pdp import PDP, PDPResult

from algoneer.result import DatasetModelResult

import unittest

class TestPDP(unittest.TestCase):

    def test_pdp(self) -> None:

        # we load the dataset
        dataset = load_dataset()
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm('linear-regression')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        # we initialize a PDP test
        pdp = PDP()

        columns = ['windspeed', 'hum', 'atemp', 'season']

        # we run the PDP test on the model and dataset
        result = pdp.run(dataset, model, columns=columns, max_datapoints=110, max_values=5)

        # we make sure that we obtain a reasonable result
        assert isinstance(result, DatasetModelResult)
