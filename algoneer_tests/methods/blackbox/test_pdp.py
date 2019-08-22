from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.algorithms import get_algorithm, algorithms
from algoneer.methods.blackbox.pdp import PDP

def test_pdp():

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
    result = pdp.run(model, dataset, columns=columns, max_datapoints=110, max_values=5)

    # we make sure that we obtain a reasonable result
    assert result