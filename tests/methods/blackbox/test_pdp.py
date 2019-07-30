from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.pdp import PDP

def test_pdp():

    # we load the dataset
    dataset = load_dataset()
    
    # we select an algorithm from the set of algorithms
    algo = get_algorithm('logistic-regression')

    # we train the algorithm with the dataset to obtain a model
    model = algo.fit(dataset)

    # we initialize a PDP test
    pdp = PDP()

    # we run the PDP test on the model and dataset
    result = pdp.run(model, dataset)

    # we make sure that we obtain a reasonable result
    assert result