from algoneer.dataschema import AttributeSchema, DataSchema

def test_dataschema():

    class MySchema(DataSchema):

        temperature = AttributeSchema(type=AttributeSchema.Type.Numerical, roles=["x"])

    schema = MySchema()

    assert hasattr(schema, 'temperature')
    assert hasattr(schema, 'attributes')
    assert isinstance(schema.attributes['temperature'], AttributeSchema)
    assert schema.attributes['temperature'] is not MySchema.temperature

    schema_copy = schema.copy()

    assert schema_copy is not schema
    assert schema_copy.attributes['temperature'] is not schema.attributes['temperature']

    assert schema_copy.attributes['temperature'].type == AttributeSchema.Type.Numerical
    assert schema_copy.attributes['temperature'].roles == ['x']
