from typing import Optional, Iterable, Dict, Any, List

import functools
import pandas as pd
import os
import yaml

from .dataset import DataSet
from .roles import Roles
from .attribute import Attribute
from algoneer.dataschema import DataSchema, AttributeSchema


def proxy(f):
    @functools.wraps(f)
    def convert(self, *args, **kwargs):
        nargs = []
        nkwargs = {}
        for arg in args:
            if isinstance(arg, PandasAttribute):
                nargs.append(arg.column)
            else:
                nargs.append(arg)

        for k, v in kwargs.items():
            if isinstance(arg, PandasAttribute):
                nkwargs[k] = v.column
            else:
                nkwargs[k] = v
        return f(self, *args, **kwargs)

    return convert

class PandasAttribute(Attribute):
    def __init__(
        self,
        dataset: "PandasDataSet",
        series: pd.Series,
        schema: Optional[AttributeSchema] = None,
    ) -> None:

        d = self.__dict__

        d["_dataset"] = dataset
        d["_schema"] = schema
        d["_column"] = series.name
        d["_series"] = series

    @property
    def schema(self) -> Optional[AttributeSchema]:
        return self._schema

    @schema.setter
    def schema(self, schema: Optional[AttributeSchema]) -> None:
        self._schema = schema

    @property
    def roles(self) -> Iterable[str]:
        if self._schema is None:
            return []
        return self._schema.roles

    @property
    def column(self) -> str:
        return self._column

    @column.setter
    def column(self, column: str) -> None:
        self._column = column

    @proxy
    def __setitem__(self, item, value):
        return self._series.__setitem__(item, value)

    @proxy
    def __delitem__(self, item):
        return self._series.__delitem(item)

    def __getattr__(self, attr):
        v = getattr(self._series, attr)
        # if this is a callable function we wrap it in a proxy decorator
        if callable(v):
            return proxy(v)
        return v

    def __setattr__(self, attr, value):
        return setattr(self._series, attr, value)

    def astype(self, type: str, **kwargs: Dict[str, Any]):
        pass


class PandasDataSet(DataSet):

    """
    An implementation of a :class:`~algoneer.dataset.DataSet` object relying
    on a :class:`pandas.DataFrame`.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        # we need to use __dict__ since we overwrote the __getattr__ function
        self.__dict__["_df"] = df
        attributes: List[PandasAttribute] = []
        for column in self.columns:
            attributes.append(PandasAttribute(self, df[column]))
        self.__dict__["_attributes"] = attributes

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @proxy
    def __getitem__(self, item):
        v = self._df.__getitem__(item)
        if isinstance(v, pd.DataFrame):
            ds = PandasDataSet(v)
            ds.schema = self.schema
            return ds
        elif isinstance(v, pd.Series):
            return PandasAttribute(self, v)
        return v

    @proxy
    def __setitem__(self, item, value):
        return self._df.__setitem__(item, value)

    @proxy
    def __delitem__(self, item):
        return self._df.__delitem(item)

    def __getattr__(self, attr):
        v = getattr(self._df, attr)
        # if this is a callable function we wrap it in a proxy decorator
        if callable(v):
            return proxy(v)
        return v

    def __setattr__(self, attr, value):
        return setattr(self._df, attr, value)

    @property
    def columns(self) -> Iterable[str]:
        return self._df.columns

    @property
    def attributes(self) -> Iterable[PandasAttribute]:
        return self._attributes

    @property
    def schema(self) -> DataSchema:
        return self._schema

    @schema.setter
    def schema(self, schema: DataSchema) -> None:
        self._schema = schema

    def copy(self) -> "PandasDataSet":

        # we initialize a new dataset with a copy of the dataframe
        ds = PandasDataSet(self._df.copy())
        # we copy the schema as well
        ds.schema = self.schema

        return ds

    def astype(self, type: str, **kwargs: Dict[str, Any]):
        pass

    # Static helper methods (to create PandasDataSet objects)

    @staticmethod
    def from_dataset(dataset: DataSet) -> "PandasDataSet":
        if not isinstance(dataset, PandasDataSet):
            raise ValueError("cannot convert to PandasDataSet right now")
        # we simply make a copy of the dataset
        return dataset.copy()

    @staticmethod
    def from_path(path: str) -> "PandasDataSet":
        spec_filename = os.path.join(path, "dataset.yml")

        if not os.path.isfile(spec_filename):
            raise IOError("file '{}' not found".format(spec_filename))

        with open(spec_filename) as spec_file:
            d = spec_file.read()

        c = yaml.load(d, Loader=yaml.BaseLoader)
        l = c.get("loader", {})
        t = l.get("type")
        a = l.get("args", {})

        if t == "csv":
            df = pd.read_csv(os.path.join(path, a.get("filename")))
        else:
            raise ValueError("no loader for type {}".format(t))

        ds = PandasDataSet(df)

        # we assign the data schema to the dataset
        schema = DataSchema(c.get("schema", {}))

        # we enforce the data schema on the dataset
        schema.enforce(ds)
        ds.schema = schema

        return ds
