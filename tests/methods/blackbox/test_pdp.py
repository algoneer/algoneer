from algoneer_datasets.bike_sharing import load_dataset
from algoneer_datasets.bike_sharing.models import get_model, models

def test_pdp():
    dataset = load_dataset()
    model = get_model('logistic-regression')