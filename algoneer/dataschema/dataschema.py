from typing import Mapping, Dict, Any, Optional

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


class DataSchema(metaclass=DataSchemaMeta):
    def __init__(
        self,
        schema: Optional[Mapping[str, Any]] = None,
        attributes: Optional[Dict[str, AttributeSchema]] = None,
    ):
        if schema is not None:
            self._attributes = parse_attributes(self, schema)
        if attributes is None:
            for key, attribute in self.__class__._predefined_attributes.items():
                attribute.dataschema = self
                self._attributes[key] = attribute
        else:
            self._attributes = attributes

    def enforce(self, ds: "algoneer.dataset.Dataset"):
        for key, attribute in self._attributes.items():
            attribute.enforce(ds)

    @property
    def attributes(self) -> Mapping[str, AttributeSchema]:
        return self._attributes

    def copy(self) -> "DataSchema":
        new_attributes = {}
        for key, attribute in self._attributes.items():
            new_attributes[key] = attribute.copy()
        return DataSchema(attributes=new_attributes)


def parse_attributes(ds: DataSchema, schema: Mapping[str, Any]) -> Any:

    attributes: Dict[str, AttributeSchema] = {}
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
