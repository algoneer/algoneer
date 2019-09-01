from typing import (
    Optional,
    Mapping,
    Iterable,
    Dict,
    Any,
    List,
    Tuple,
    Union,
    Callable,
    Iterator,
)

import functools
import inspect
import pandas as pd
import os
import yaml

from .dataset import Dataset
from .roles import Roles
from .attribute import Attribute
from .datapoint import Datapoint
from algoneer.utils.hashing import get_hash
from algoneer.dataschema import DataSchema, AttributeSchema
from algoneer.project import Project


def proxy(
    f: Callable[..., Any], bound: bool = True, ds: "Optional[PandasDataset]" = None
) -> Callable[..., Any]:
    @functools.wraps(f)
    def convert(*args, **kwargs) -> Any:
        nargs: List[Any] = []
        nkwargs: Dict[str, Any] = {}

        dss: Optional[PandasDataset] = ds

        if bound:
            obj, args = args[0], args[1:]
            if dss is None:
                if isinstance(obj, PandasDataset):
                    dss = obj
                elif isinstance(obj, PandasAttribute):
                    dss = obj.dataset

        def wrap(
            v: Any, ds: PandasDataset
        ) -> Union[PandasAttribute, PandasDataset, Any]:
            if isinstance(v, pd.DataFrame):
                nds = PandasDataset(ds.project, ds.schema[set(v.columns)], v)
                return nds
            elif isinstance(v, pd.Series):
                schema = ds.schema.attributes.get(v.name)
                assert schema is not None
                return PandasAttribute(ds, v.name, schema, v)
            return v

        def conv(arg: Any) -> Any:
            if isinstance(arg, PandasAttribute):
                return arg.series
            elif isinstance(arg, PandasDataset):
                return arg.df
            return arg

        for arg in args:
            nargs.append(conv(arg))

        for k, v in kwargs.items():
            nkwargs[k] = conv(v)

        if bound:
            res = f(obj, *nargs, **nkwargs)
        else:
            res = f(*nargs, **nkwargs)

        if isinstance(dss, PandasDataset):
            return wrap(res, dss)

        return res

    return convert


class PandasDatapoint(Datapoint):
    def __init__(self, dataset: "PandasDataset", index: Any) -> None:
        self._dataset = dataset
        self._index = index

    @property
    def dataset(self) -> Dataset:
        return self._dataset

    @property
    def index(self) -> Any:
        return self._index

    @property
    def data(self) -> Dict[str, Any]:
        return self._dataset.df.iloc[self._index : self._index + 1].to_dict(
            orient="rows"
        )[0]

    @property
    def hash(self) -> Optional[bytes]:
        return get_hash(self.data)

    def copy(self) -> "PandasDatapoint":
        return PandasDatapoint(self._dataset, self._index)


class PandasAttribute(Attribute):
    def __init__(
        self,
        dataset: "PandasDataset",
        column: str,
        schema: AttributeSchema,
        series: pd.Series,
    ) -> None:

        super().__init__(dataset, column, schema)

        d = self.__dict__
        d["_series"] = series

    @property
    def series(self) -> pd.Series:
        return self._series

    def sum(self) -> float:
        return self._series.sum()

    def mean(self) -> float:
        return self._series.mean()

    def min(self) -> float:
        return self._series.min()

    def max(self) -> float:
        return self._series.max()

    @proxy
    def __getitem__(self, item):
        return self._series.__getitem__(item)

    @proxy
    def __setitem__(self, item, value):
        return self._series.__setitem__(item, value)

    @proxy
    def __delitem__(self, item):
        return self._series.__delitem(item)

    def __len__(self) -> int:
        return len(self._series)

    def __getattr__(self, attr):

        try:
            return super().__getattr__(attr)
        except AttributeError:
            pass

        v = getattr(self._series, attr)
        # if this is a callable function we wrap it in a proxy decorator
        if callable(v) and not inspect.isclass(v):
            return proxy(v, bound=False, ds=self)
        return v

    def astype(self, type: str, config: Dict[str, Any]):
        # to do: implement this
        return self


class PandasDataset(Dataset):

    """
    An implementation of a :class:`~algoneer.dataset.Dataset` object relying
    on a :class:`pandas.DataFrame`.
    """

    def __init__(self, project: Project, schema: DataSchema, df: pd.DataFrame) -> None:
        # we need to use __dict__ since we overwrote the __getattr__ function
        super().__init__(project, schema)
        # we only select the relevant columns from the dataframe
        rdf = df[list(schema.attributes.keys())]
        self.__dict__["_df"] = rdf
        self._generate_attributes()

    def _generate_attributes(self) -> None:
        attributes: Dict[str, PandasAttribute] = {}
        schema = self.schema
        for column in self.columns:
            attributeschema = schema.attributes[column]
            attributes[column] = PandasAttribute(
                self, column, attributeschema, self._df[column]
            )
        self.__dict__["_attributes"] = attributes

    def datapoint(self, index: Any) -> PandasDatapoint:
        return PandasDatapoint(self, index)

    @property
    def hash(self) -> Optional[bytes]:
        hashes = []
        for record in self._df.to_dict(orient="records"):
            hashes.append(get_hash(record))
        hashes = sorted(hashes)
        return get_hash(hashes)

    @property
    def df(self) -> pd.DataFrame:
        return self._df

    @proxy
    def __getitem__(self, item) -> Union["PandasDataset", PandasAttribute]:
        v = self._df.__getitem__(item)
        return v

    @proxy
    def __setitem__(self, item, value):
        return self._df.__setitem__(item, value)

    @proxy
    def __delitem__(self, item):
        return self._df.__delitem(item)

    def __iter__(self) -> Iterator:
        return self._df.iterrows()

    def __len__(self) -> int:
        return len(self._df)

    def __getattr__(self, attr):

        try:
            return super().__getattr__(attr)
        except AttributeError:
            pass

        v = getattr(self._df, attr)
        # if this is a callable function we wrap it in a proxy decorator
        if callable(v) and not inspect.isclass(v):
            return proxy(v, bound=False, ds=self)
        return v

    @property
    def columns(self) -> Iterable[str]:
        return self._df.columns

    @property
    def attributes(self) -> Mapping[str, PandasAttribute]:
        return self._attributes

    @property
    def shape(self) -> Tuple:
        return self._df.shape

    def sum(self) -> float:
        return self._df.sum()

    def mean(self) -> float:
        return self._df.mean()

    @proxy
    def select(
        self, indexes: Union[int, Iterable[int], slice], copy: bool = True
    ) -> "PandasDataset":
        ndf = self._df.iloc[indexes, :]
        if copy:
            return ndf.copy()
        return ndf

    def copy(self) -> "PandasDataset":

        # we initialize a new dataset with a copy of the dataframe
        ds = PandasDataset(self.project, self.schema.copy(), self._df.copy())
        # we copy the schema as well
        ds.schema = self.schema

        return ds

    def astype(self, type: str, **kwargs: Dict[str, Any]):
        # to do: implement this
        pass

    # Static helper methods (to create PandasDataset objects)

    @staticmethod
    def from_dataset(dataset: Dataset) -> "PandasDataset":
        if not isinstance(dataset, PandasDataset):
            raise ValueError("cannot convert to PandasDataset right now")
        # we simply make a copy of the dataset
        return dataset.copy()

    @staticmethod
    def from_path(project: Project, path: str) -> "PandasDataset":
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

        # we assign the data schema to the dataset
        schema = DataSchema(c.get("schema", {}))
        ds = PandasDataset(project, schema, df)

        return ds

    def __sub__(self, other: "Dataset") -> "PandasDataset":
        assert isinstance(other, PandasDataset)
        ds = PandasDataset(self.project, self.schema, self.df - other.df)
        return ds

    def __add__(self, other: "Dataset") -> "PandasDataset":
        assert isinstance(other, PandasDataset)
        ds = PandasDataset(self.project, self.schema, self.df + other.df)
        return ds

    @proxy
    def order_by(self, columns: Iterable[str]) -> "PandasDataset":
        return self.df.sort_values(columns).reset_index(drop=True)
