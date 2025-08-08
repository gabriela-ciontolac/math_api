from pydantic import BaseModel

class FactorialRequest(BaseModel):
    n: int

class FactorialResponse(BaseModel):
    result: int