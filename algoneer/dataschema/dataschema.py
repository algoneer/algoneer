from typing import Mapping, Dict, Any

from .attributeschema import AttributeSchema
import algoneer.dataset


class DataSchema:
    def __init__(self, schema: Mapping[str, Any]):
        self._schema = parse_schema(self, schema)
        self._attributes = parse_attributes(self, schema)

    def enforce(self, ds: "algoneer.dataset.DataSet"):
        for key, attribute in self._attributes.items():
            attribute.enforce(ds)

    @property
    def attributes(self) -> Mapping[str, AttributeSchema]:
        return self._attributes


def parse_schema(ds: DataSchema, schema: Mapping[str, Any]) -> Any:
    return schema


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
            ds, column=key, type=_type, config=config, roles=roles
        )
    return attributes
