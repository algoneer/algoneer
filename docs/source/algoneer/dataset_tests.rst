Dataset Tests
=============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Machine learning models are trained with data. Carefully preparing and
validating datasets is important to ensure good learning results. Many problems
around robustness, fairness, accountability and security of ML models are
directly or indirectly related to problems in the training data.

Algoneer therefore provides a wide range of tests that operate on datasets
and help you to detect and fix problems in your training data early. Some of
these tests also help you to gain a better understanding of your training data
in general, which is useful e.g. for feature selection.

The following list contains a number of dataset tests that are relevant for
ML systems and their availability in Algoneer.

If you miss a test that you think is relevant please add it and open a pull
request.

General Remarks
---------------

To decide which tests to run on a given dataset Algoneer uses the
:doc:`data schema <./data_schema>` of the dataset. If no schema is
Algoneer will be restricted in the number of tests it can run on the dataset.
Therefore, before running the dataset tests please make sure you have defined
a valid data schema.

Running Tests
-------------

To run dataset tests, simply create a `DataSet` instance as well as an
Algoneer instance and run the tests:

.. code-block:: python

   from algoneer import Dataset, Algorithm, Model, Schema

   # create e.g. a Pandas dataframe
   df = pandas.DataFrame(...)

   # create a schema for the data
   schema = Schema(...)

   # create a dataset
   dataset = Dataset(df, schema)

   # run the tests
   result = dataset.test()


List of Tests / Test Roadmap
----------------------------

The following list contains the different dataset-related tests that are either
already implemented in Algoner or that we plan to implement. You can provide
feedback on our feature roadmap by opening an issue on
`Github <https://github.com/algoneer/docs/issues>`_.

* **Distribution Analysis**: Provides basic information about the distribution of
  individual features and feature combinations, and detects possible problems
  or anomalies in the distribution.
* **Correlation Analysis**: Analyzes feature correlations and potential problems
  such as redundant or strongly correlated features.
* **Sensitive Attribute Analysis**: Analyzes the correlation and predictability of
  sensitive attributes in the dataset.
* **Feature Space Analysis**: Analyzes the coverage of the feature space by the
  datasets, and potential problems when using the data for machine learning.
* **Time-Dependent Analysis**: Analyzes if and how the distribution of features
  changes over time, and detects possible problems due to non-stationary
  data distribution.
* **Bias Detection**: Detects potential biases regarding sensitive attributes.
* **Outlier Detection**: Detects outliers and anomalous datapoints in the dataset.
* **Quality Problem Detection**: Detects missing data values or other quality
  problems in the dataset.
* **Prototypes and Criticisms**: Generates datapoints that are representative of
  the dataset (prototypes) as well as datapoints that are not representative
  (criticisms).

Did we miss anything important? Please let us know by opening an 
`issue <https://github.com/algoneer/docs/issues>`_ on our issue tracker.