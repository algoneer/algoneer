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

    You need at least Python version 3.6 to run Algoneer.

.. code-block:: bash

    pip3 install algoneer

Algoneer aims to be technology-agnostic and provides wrappers for the most
popular data processing and machine learning libraries. In this tutorial, we
are going to use Algoneer in conjunction with `pandas` and `scikit-learn`. In 
case you have not installed them already, you can do so by executing:

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
    example code `on GitHub <https://github.com/algoneer/algoneer/blob/master/examples/bike-sharing/partial-dependence-plot.ipynb>`_.

.. code-block:: python

    from algoneer_datasets.bike_sharing import load_dataset
    ds = load_dataset()

This creates a :class:`~algoneer.dataset.pandas.PandasDataSet` that contains
the bike sharing data. This dataset is just a thin wrapper around a pandas
dataframe and adds functionality that is helpful when using the dataset for
testing. Notably, it includes a :class:`~algoneer.dataschema.DataSchema` that
contains information about all attributes in the dataset.

Now, to test a machine learning model with Algoneer we first need to train one.
To do this, we can again import a model from the example datasets library:

.. code-block:: python

    from algoneer_datasets.bike_sharing.algorithms import get_algorithm
    algo = get_algorithm('random-forest', n_estimators=100)
    model = algo.fit(ds)

Again, the :class:`~algoneer.algorithm.Algorithm` class is just a thin wrapper
around existing algorithms, in this case a scikit-learn random forest regressor.

Now that we have trained our model, we can run a simple black box test on it:

.. code-block:: python

    from algoneer.methods.blackbox.pdp import PDP

    pdp = PDP()

This so-called partial dependence plot is a simple test that quantifies the
average effect that a given attribute has on the prediction of a machine
learning model. You can read more about the test
`here <https://christophm.github.io/interpretable-ml-book/pdp.html>`_.

Let's run it on our model:

.. code-block:: python

    result = pdp.run(model, ds, max_values=20, max_datapoints=100)

Here, `max_values` specifies the maximum number of distinct values of each
attribute that we will calculate the dependence for, `max_datapoints` specifies
the number of datapoints that we use to average the effect of the attribute.
The PDP test will calculate the dependence values for all attributes in the
dataset that have a `x` role. You can restrict the attributes for which you
want to calculate the dependence by specifying a list of attribute columns
that you're interested in using the `columns` parameter.

Currently, the result that we obtain is a simple data structure that contains
a list of tuples for each attribute, which contains the average predicted
value for the different attribute values. We're working on a better presentation
of these results, please bear with us.