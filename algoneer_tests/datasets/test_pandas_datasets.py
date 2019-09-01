from algoneer_datasets.bike_sharing import load_dataset
from algoneer.dataset import Dataset
from algoneer.project import Project

import unittest

class PandasDatasetTest(unittest.TestCase):

    def test_sklean(self):

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)

        assert isinstance(dataset, Dataset)

        hash = dataset.hash

        assert hash == b'\x01\x00\x00\x00\xb9\x96\xdb_\xdc\xe6\x98\x05\xe0\xe5\xec`HQ\x82\x14\xde[o5\n\xff\xd2\xb1\xe2K\x06>\xd1:M\xf9'

        datapoint = dataset.datapoint(0)
        dp_hash = datapoint.hash
        assert dp_hash == b'\x01\x00\x00\x00E/\xbdy\xbe#\x19g\xf3\xafV\x1a\xe3\x84\xeel{:\xde)\xa0\x89e\xc1\xbf\xd9\xc6\x94\x8a\x90G\xde'

