from .blackbox import dataset_model_tests as blackbox_dataset_model_tests
from algoneer import DatasetModelTest

from typing import Type, List

dataset_model_tests: List[Type[DatasetModelTest]] = []

dataset_model_tests.extend(blackbox_dataset_model_tests)
