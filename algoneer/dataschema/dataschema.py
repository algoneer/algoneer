from typing import Mapping, Any

from .attributeschema import AttributeSchema


class DataSchema:
    def __init__(self, schema: Mapping[str, Any]):
        self._schema = parse_schema(self, schema)
        self._attributes = parse_attributes(self, schema)


def parse_schema(ds: DataSchema, schema: Mapping[str, Any]) -> Any:
    return schema


def parse_attributes(ds: DataSchema, schema: Mapping[str, Any]) -> Any:

    attributes = []
    for key, attribute in schema.get("attributes", {}).items():
        typestring = attribute.get("type", "unknown")
        try:
            _type = AttributeSchema.Type[typestring.capitalize()]
        except KeyError:
            _type = AttributeSchema.Type.Unknown
        config = attribute.get("config", {})
        attributes.append(AttributeSchema(ds, column=key, type=_type, config=config))
    return schema
