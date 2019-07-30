from typing import Optional, List

import pandas as pd
import os
import yaml

from .dataset import DataSet
from .roles import Roles
from algoneer.dataschema import DataSchema, AttributeSchema

class PandasRoles(Roles):

    def __init__(self, dataset : 'PandasDataSet') -> None:
        self._dataset = dataset

    def __getattr__(self, attr) -> 'PandasDataSet':
        """
        We return a dataset with all attributes that have the given role
        """
        return self._dataset

class PandasAttribute:
    
    def __init__(self, dataset : 'PandasDataSet', column : str, schema : Optional[AttributeSchema] = None) -> None:
        self._dataset = dataset
        self._schema = schema
        self._column = column

    @property
    def schema(self) -> Optional[AttributeSchema]:
        return self._schema

    @schema.setter
    def schema(self, schema : AttributeSchema) -> None:
        self._schema = schema

    @property
    def column(self) -> str:
        return self._column

    @column.setter
    def column(self, column :str) -> None:
        self._column = column

class PandasDataSet(DataSet):

    """
    An implementation of a :class:`~algoneer.dataset.DataSet` object relying
    on a :class:`pandas.DataFrame`.
    """

    def __init__(self, df : pd.DataFrame) -> None:
        self._df = df
        attributes : List[PandasAttribute] = []
        for column in df.columns:
            attributes.append(PandasAttribute(self, column))
        self._attributes = attributes


    @property
    def df(self) -> pd.DataFrame:
        return self._df

    def __getitem__(self, *args, **kwargs):
        return self._df.__getitem__(*args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        return self._df.__setitem__(*args, **kwargs)

    def enforce_schema(self, schema: DataSchema) -> None:
        pass

    def copy(self) -> 'PandasDataSet':
        ds = PandasDataSet(self._df.copy())
        return ds
 
    @property
    def attributes(self) -> List[PandasAttribute]:
        return self._attributes

    @property
    def roles(self) -> PandasRoles:
        return PandasRoles(self)

    # Static helper methods (to create PandasDataSet objects)

    @staticmethod
    def from_dataset(dataset : DataSet) -> 'PandasDataSet':
        if not isinstance(dataset, PandasDataSet):
            raise ValueError("cannot convert to PandasDataSet right now")
        # we simply make a copy of the dataset
        return dataset.copy()

    @staticmethod
    def from_path(path : str) -> 'PandasDataSet':
        spec_filename = os.path.join(path, 'dataset.yml')

        if not os.path.isfile(spec_filename):
            raise IOError("file '{}' not found".format(spec_filename))

        with open(spec_filename) as spec_file:
            d = spec_file.read()

        c = yaml.load(d, Loader=yaml.BaseLoader)
        l = c.get('loader', {})
        t = l.get('type')
        a = l.get('args', {})

        if t == 'csv':
            df = pd.read_csv(os.path.join(path, a.get('filename')))
        else:
            raise ValueError("no loader for type {}".format(t))

        ds = PandasDataSet(df)

        schema = DataSchema(c.get('schema', {}))

        ds.enforce_schema(schema)

        return ds
