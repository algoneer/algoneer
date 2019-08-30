from .blackbox import model_tests as blackbox_model_tests
from algoneer.modeltest import ModelTest

from typing import Type, List

model_tests: List[Type[ModelTest]] = []

model_tests.extend(blackbox_model_tests)
