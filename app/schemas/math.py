from pydantic import BaseModel

class PowRequest(BaseModel):
    base: float
    exp: float

class PowResponse(BaseModel):
    result: float

class FibonacciRequest(BaseModel):
    n: int

class FibonacciResponse(BaseModel):
    result: int

class FactorialRequest(BaseModel):
    n: int

class FactorialResponse(BaseModel):
    result: int