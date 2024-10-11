from pydantic import BaseModel

class TrainSchema(BaseModel):
    first_row: str
    second_row: str

class TrainSchemaPeople(BaseModel):
    name: str
    surname: str
    age: int

class TrainSchemaName(BaseModel):
    name: str

