from pydantic import BaseModel

class PowRequest(BaseModel):
    base: float
    exp: float

class PowResponse(BaseModel):
    result: float