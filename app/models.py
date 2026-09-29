from pydantic import BaseModel

class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    rate: float
    result: float