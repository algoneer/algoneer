Getting Started
===============

.. attention::

   This is a work-in-progress that shows how the pre-alpha version of Algoneer
   works. Please let us know if you should encounter any problems.

Algoneer provides blackbox tests that work on :class:`~algoneer.model.Model`
objects. A Model is an :class:`~algoneer.algorithm.Algorithm` that has been
trained with a specific :class:`~algoneer.dataset.DataSet`.

To get started we need to install Algoneer.

.. note::

    You need Python version >=3.6 to run Algoneer.

.. code-block:: bash

    pip3 install algoneer

Algoneer aims to be technology-agnostic and provides wrappers for the most
popular data processing and machine learning libraries. In this tutorial, we
are going to use Algoneer in conjunction with `pandas` and `scikit-learn`. In 
case you have not installed them already, you can do so by running:

.. code-block:: bash

    pip3 install pandas scikit-learn

Algoneer also provides a separate package with several example datasets that
make it easy to get started. We can also install them using pip:

.. code-block:: bash

    pip3 install algoneer_datasets

That's it, we're good to go! Let's start using Algoneer by loading an example
dataset and running a test on it. 

.. note::
    You can find the whole
    example code `on GitHub <https://github.com/algoneer/algoneer/tree/master/examples/bike-sharing>`_.

.. code-block:: python

    from algoneer.dataschema import DataSchema, AttributeSchema as AS

    # we define the data schema for the bike dataset, which helps Algoneer to automatically
    # run tests on the dataset and any models derived from it

    class BikeSchema(DataSchema):

        # these are the regressands, which have the "x" role
        instant = AS(type=AS.Type.Integer, roles=["x"])
        season = AS(type=AS.Type.Categorical, roles=["x"])
        yr = AS(type=AS.Type.Integer, roles=["x"])
        mnth = AS(type=AS.Type.Integer, roles=["x"])
        holiday = AS(type=AS.Type.Boolean, roles=["x"])
        weekday = AS(type=AS.Type.Integer, roles=["x"])
        workingday = AS(type=AS.Type.Boolean, roles=["x"])
        weathersit = AS(type=AS.Type.Categorical, roles=["x"])
        temp = AS(type=AS.Type.Numerical, roles=["x"])
        atemp = AS(type=AS.Type.Numerical, roles=["x"])
        hum = AS(type=AS.Type.Numerical, roles=["x"])
        windspeed = AS(type=AS.Type.Numerical, roles=["x"])

        # this is the regressor, which has the "y" role
        cnt = AS(type=AS.Type.Integer, roles=["y"])

.. code-block:: python

    from algoneer_datasets.bike_sharing import path
    from algoneer.dataset.pandas import PandasDataset

    # we read the CSV data into a pandas dataframe
    import pandas as pd
    df = pd.read_csv(path+'/data.csv.gz')

    # we wrap the dataframe with an Algoneer dataset using the bike schema
    ds = PandasDataset(BikeSchema(), df)

This creates a :class:`~algoneer.dataset.pandas.PandasDataSet` that contains
the bike sharing data. This dataset is just a thin wrapper around a pandas
dataframe and adds functionality that is helpful when using the dataset for
testing. Notably, it includes a :class:`~algoneer.dataschema.DataSchema` that
contains information about all attributes in the dataset.

Now, to test a machine learning model with Algoneer we first need to train one.
To do this, we can again import a model from the example datasets library:

.. code-block:: python

    from sklearn.ensemble import RandomForestRegressor
    from algoneer.algorithm.sklearn import SklearnAlgorithm

    # we wrap the random forest classifier using the SklearnAlgorithm class
    algo = SklearnAlgorithm(RandomForestRegressor, n_estimators=100)

    # we produce a model by training the algorithm with a dataset
    model = algo.fit(ds)

Again, the :class:`~algoneer.algorithm.Algorithm` class is just a thin wrapper
around existing algorithms, in this case a scikit-learn random forest regressor.

Now that we have trained our model, we can run a simple black box test on it:

.. code-block:: python

    from algoneer.methods.blackbox.shap import SHAP

    shap = SHAP()

This so-called partial dependence plot is a simple test that quantifies the
average effect that a given attribute has on the prediction of a machine
learning model. You can read more about the test
`here <https://christophm.github.io/interpretable-ml-book/pdp.html>`_.

Let's run it on our model:

.. code-block:: python

    result = shap.run(model, ds, max_datapoints=100)

Here, `max_datapoints` specifies the number of datapoints that we use to average the effect of
the attribute.
