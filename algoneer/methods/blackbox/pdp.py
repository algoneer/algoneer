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
        self, model: Model, dataset: DataSet, attributes: Optional[Sequence[str]] = None
    ):
        """
        Run the test.

        :param    model: The model for which to generate the PDP.
        :param  dataset: The dataset for which to generate the PDP.
        :param attributes: The attributes for which to generate the PDP. Optional.
        """

        def pdp(ds, model, column):
            """
            Generate the partial dependence for a categorical attribute
            """
            attribute = dataset[column]
            if attribute.is_categorical or attribute.is_ordinal:
                # we get all unique values for the attribute
                vs = attribute.unique()
            elif attribute.is_numerical:
                vs = attribute.unique()
            else:
                raise ValueError("unknown attribute type: {}".format(attribute.type))

            vs.assign(pdp=0)

            for i, v in vs.iterrows():
                # we make a copy of the dataset (this might be expensive)
                nds = ds.copy()
                # we replace all values of the attribute by v
                nds[column] = v
                # we compute the prediction of the model for the modified data
                y = model.predict(nds)
                if model.is_classifier:
                    # to do: handle multi-class classifiers
                    # if this is a classifier we calculate the probability
                    vs[i, "pdp"] = y.sum() / len(y)
                elif model.is_regression:
                    # if this is a regression, we calculate the mean value
                    vs[i, "pdp"] = y.mean()

            return vs

        # we store PDPs in a simple dict
        pdps = {}

        # we generate a partial dependence plot for every column
        for column in dataset.columns:
            pdps[column] = pdp(dataset, model, column)

        # we return the PDPs
        return pdps
