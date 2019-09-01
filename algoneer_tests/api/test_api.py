from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm
from algoneer.dataschema import AttributeSchema, DataSchema
from algoneer.methods.blackbox.ale import ALE, ALEResult
from algoneer.api import Session, Response, Object as APIObject
from algoneer.api.base_client import BaseClient
from algoneer.object import Object
from algoneer.api.object import mappings
from algoneer.model import Model
from algoneer.project import Project

import unittest

class Client(BaseClient):

    def get(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def post(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def patch(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def delete(self, url: str, **kwargs) -> Response:
        return Response(200, {})

class ApiTest(unittest.TestCase):

    def test_objects(self) -> None:

        project = Project("test")

        # we load the dataset
        dataset = load_dataset(project)
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm(project, 'linear-regression')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        assert isinstance(algo, Object)
        assert isinstance(model, Object)
        assert isinstance(dataset, Object)


        # we initialize a ALE test
        ale = ALE()

        columns = ['windspeed', 'hum', 'atemp', 'season']

        # we run the ALE test on the model and dataset
        result = ale.run(dataset, model, columns=columns, max_datapoints=200, n_intervals=10)

        client = Client()
        session = Session(client)

        api_model = session.add(model)
        api_dataset = session.add(dataset)
        api_algo = session.add(algo)
        api_result = session.add(result)

        assert model in session
        assert dataset in session
        assert algo in session
        assert result in session

        session.sync()
