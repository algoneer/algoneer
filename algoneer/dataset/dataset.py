from typing import Union, Optional

try:
    import pandas as pd

    with_pandas = True
except ImportError:
    with_pandas = False

try:
    import numpy as np

    with_numpy = True
except ImportError:
    with_numpy = False


class DataSet:

    """Describes a collection of :class:`~algoneer.datapoint.DataPoint` objects.
    """

    def __init__(self, source=Optional[Union["pandas.DataFrame", "numpy.ndarray"]]):
        pass

ds = DataSet(pd.DataFrame())