Getting Started
===============

Algoneer helps you to better understand your datasets and machine learning
models and test them for potential problems. Using Algoneer is very simple.

Testing DataSets
----------------


Testing Models
--------------

Algoneer provides blackbox tests that work on :class:`~algoneer.model.Model`
objects. A Model is an :class:`~algoneer.algorithm.Algorithm` that has been
trained with a specific :class:`~algoneer.dataset.DataSet`.

As an example, we're going to load an example dataset:

.. code-block:: python

    from sklearn.datasets import load_wine
   
    data = load_wine()

    import pandas as pd
    import numpy as np

    Y = pd.DataFrame(data['target'],)[0]
    features= [[i, "f{}".format(i+1)] for i in range(13)]
    X = pd.DataFrame(data['data'][:,[f[0] for f in features]], columns=[f[1] for f in features])

Then, we're going to define a test and training dataset:

.. code-block:: python

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

Let's train a classifier with this data:

.. code-block:: python

    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    clf.fit(X_train, Y_train)

    # we produce predictions for the training set
    Yp_train = clf.predict(X_train)

That's it! Let's see what our accuracy is:

.. code-block:: python

    from sklearn.metrics import accuracy_score
    print("Training data accuracy: {:.2f}".format(accuracy_score(Yp_train, Y_train)*100))
    # Training data accuracy: 98.88

Pretty good! But let's investigate this result with Algoneer. To do so, we
first create a :class:`~algoneer.model.Model` instance:

.. code-block:: python

   
    from algoneer import Model, DataSet

    # we create a dataset for the training data
    ds = DataSet(X=X_train, Y=Y_train)

    # we create a model from our classifier and the training dataset
    model = Model(clf, dataset=ds)

That's all we need to start testing, as Algoneer will automatically detect
what kind of model we created and what it can do with it. To run all available
tests on the model, we simply run

.. code-block:: python

    results = model.test()

The `result` variable will contain a :class:`~algoneer.result_set.ResultSet`
instance which will in turn contain results for all tests that Algoneer
executed on the model and the dataset.

To investigate results directly in Python, we can do the following:

.. code-block:: python

    robustness = results['robustness']
    robustness.report(format='stdout')

This will print the test result as a text to the standard output. To document
your test results more permanently we can upload them to the
:doc:`Algonaut <algonaut/index>` service. For this, we first need to generate an
:doc:`access token <algonaut/access_tokens>`. After doing that, we can
simply initialize a :class:`~algoneer.session.Session` object and use it to
upload the results:

.. code-block:: python

    from algoneer import Session

    session = Session('our-api-token-value')

    session.add(results)
    session.sync()

Voila! Our results will now be available on Algonaut, where we can interact
them using a rich user interface and where we can share them with our team
mates.