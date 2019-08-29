from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.shap import SHAP, SHAPDatapointResult, SHAPModelResult

import math

def test_shap():

    # we load the dataset
    dataset = load_dataset()
    
    # we select an algorithm from the set of algorithms
    algo = get_algorithm('linear-regression')

    # we train the algorithm with the dataset to obtain a model
    model = algo.fit(dataset)

    # we initialize a SHAP test
    shap = SHAP()

    # we run the SHAP test on the model and dataset
    result = shap.run(model, dataset, max_datapoints=10)

    # we make sure that we obtain a reasonable result
    assert isinstance(result, SHAPModelResult)

    assert 'expected_value' in result.data
    assert math.fabs(result.data['expected_value'] - 1564.6577928309937) < 1e-7