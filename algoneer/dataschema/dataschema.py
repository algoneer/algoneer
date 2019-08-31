from typing import Mapping, Any, Optional, Set
from algoneer.object import Object
from collections import OrderedDict
from .attributeschema import AttributeSchema
import algoneer.dataset


class DataSchemaMeta(type):
    def __init__(cls, name, bases, namespace):
        attributes = {}
        for key, value in namespace.items():
            if isinstance(value, AttributeSchema):
                attributes[key] = value
        cls._predefined_attributes = attributes
        super().__init__(name, bases, namespace)


class DataSchema(Object, metaclass=DataSchemaMeta):
    def __init__(
        self,
        schema: Optional[Mapping[str, Any]] = None,
        attributes: "Optional[OrderedDict[str, AttributeSchema]]" = None,
    ):
        super().__init__()
        if schema is not None:
            self._attributes = parse_attributes(self, schema)
        else:
            self._attributes = {}
        if attributes is None:
            for key, attribute in self.__class__._predefined_attributes.items():
                attribute.dataschema = self
                self._attributes[key] = attribute.copy()
        else:
            self._attributes = attributes

    def enforce(self, ds: "algoneer.dataset.Dataset"):
        for key, attribute in self._attributes.items():
            attribute.enforce(ds)

    @property
    def attributes(self) -> Mapping[str, AttributeSchema]:
        return self._attributes

    def __getitem__(self, item: Set[str]) -> "DataSchema":
        return self.copy(attributes=item)

    def copy(self, attributes: Optional[Set[str]] = None) -> "DataSchema":
        new_attributes: "OrderedDict[str, AttributeSchema]" = OrderedDict()
        for key, attribute in self._attributes.items():
            if attributes is not None and not key in attributes:
                continue
            new_attributes[key] = attribute.copy()
        return type(self)(attributes=new_attributes)


def parse_attributes(ds: DataSchema, schema: Mapping[str, Any]) -> Any:

    attributes: "OrderedDict[str, AttributeSchema]" = OrderedDict()
    for key, attribute in schema.get("attributes", {}).items():
        typestring = attribute.get("type", "unknown")
        try:
            _type = AttributeSchema.Type[typestring.capitalize()]
        except KeyError:
            _type = AttributeSchema.Type.Unknown
        config = attribute.get("config", {})
        roles = attribute.get("roles", [])
        attributes[key] = AttributeSchema(
            column=key, type=_type, config=config, roles=roles, ds=ds
        )
    return attributes
