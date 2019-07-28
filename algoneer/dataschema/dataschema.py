from typing import Mapping, Any

def parse(schema : Mapping[str, Any]) -> Any:
    return schema

class DataSchema:
    
    def __init__(self, schema: Mapping[str, Any]):
        self._schema = parse(schema)
