from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm
from algoneer.dataschema import AttributeSchema, DataSchema
from algoneer.api import Session, Response, Object as APIObject
from algoneer.api.base_client import BaseClient
from algoneer.object import Object

from algoneer.model import Model

class Client(BaseClient):

    def get(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def post(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def patch(self, url: str, **kwargs) -> Response:
        return Response(200, {})

    def delete(self, url: str, **kwargs) -> Response:
        return Response(200, {})


import unittest

class ApiTest(unittest.TestCase):

    def test_objects(self) -> None:

        # we load the dataset
        dataset = load_dataset()
        
        # we select an algorithm from the set of algorithms
        algo = get_algorithm('linear-regression')

        # we train the algorithm with the dataset to obtain a model
        model = algo.fit(dataset)

        assert isinstance(algo, Object)
        assert isinstance(model, Object)
        assert isinstance(dataset, Object)

        client = Client()
        session = Session(client)

        session.add(model)
        session.add(dataset)
        session.add(algo)

        assert model in session
        assert dataset in session
        assert algo in session

        session.sync()
