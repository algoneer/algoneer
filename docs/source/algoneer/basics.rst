Algoneer Basics
===============

.. toctree::
   :maxdepth: 2

   algorithm
   algorithm_schema
   model
   data_set
   data_point
   data_schema
   session
   result

Algoneer is built around a handful of simple core concepts, which we introduce
in the following paragraphs. These concepts are

* :doc:`Algorithm <data_schema>`: An `Algorithm` is a well-defined method that we can train on a given `DataSet`
  to obtain a `Model`. An algorithm can contain parameters that modify its
  behavior.
* :doc:`Model <model>`: A `Model` is obtained by combining an `Algorithm` with specific parameters,
  usually by training it on a `DataSet`.
* :doc:`DataSet <data_set>`: A `DataSet` is a collection of `DataPoints` with a given `DataSchema`.
* :doc:`DataPoint <data_point>`: A `DataPoint` is a single element of a `DataSet`.
* :doc:`DataSchema <data_schema>`: A `DataSchema` describes the format of a dataset. It can be applied to a
  `DataSet` to enforce / check the data in it, or used to generate synthetic data.
* :doc:`Session <session>`: A `Session` captures all relevant information of a given test session. It can
  be used to send results, parameters and data to the Algonaut API or to
  download information from it.
* :doc:`Result <result>`: A `Result` describes the outcome of one or several `Tests` performed on either
  an `Algorithm`, `Model`, `DataSet` or combination thereof.

