"""
algoneer.methods.blackbox.pdp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This modules implements the generation of partial dependence plots for machine
learning models.
"""

from typing import Sequence, Optional
from algoneer import DataSet, Model, ModelTest

class PDP(ModelTest):

    """
    Generates a partial dependence plots for a model.
    """

    def __init__(self):
        super().__init__()

    def run(
        self, model: Model, dataset: DataSet, features: Optional[Sequence[str]] = None
    ):
        """
        Run the test.

        :param    model: The model for which to generate the PDP.
        :param  dataset: The dataset for which to generate the PDP.
        :param features: The features for which to generate the PDP. Optional.
        """

        def pdp(ds, model, feature):
            """
            Generate the partial dependence for a categorical feature
            """
            values = dataset[feature]
            if feature.is_categorical or feature.is_ordinal:
                # we get all unique values for the feature
                vs = values.unique()
            elif feature.is_numerical:
                vs = values.unique()
            else:
                raise ValueError("unknown feature type: {}".format(feature.type))

            vs.assign(pdp=0)

            for i, v in vs.iterrows():
                # we make a copy of the dataset (this might be expensive)
                nds = ds.copy()
                # we replace all values of the feature by v
                nds[feature] = v
                # we compute the prediction of the model for the modified data
                y = model.predict(nds)
                if model.is_classifier:
                    # to do: handle multi-class classifiers
                    # if this is a classifier we calculate the probability
                    vs[i, 'pdp'] = y.sum()/len(y)
                elif model.is_regression:
                    # if this is a regression, we calculate the mean value
                    vs[i, 'pdp'] = y.mean()

            return vs

        # we store PDPs in a simple dict
        pdps = {}

        # we generate a partial dependence plot for every feature
        for feature in dataset.features:
            pdps[feature] = pdp(dataset, model, feature)

        # we return the PDPs
        return pdps
