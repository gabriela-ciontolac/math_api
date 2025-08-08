from pydantic import BaseModel

class FibonacciRequest(BaseModel):
    n: int

class FibonacciResponse(BaseModel):
    result: int