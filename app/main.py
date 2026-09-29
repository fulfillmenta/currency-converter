from fastapi import FastAPI, HTTPException
from app.models import ConversionResponse
from app.services import get_exchange_rate, convert


app = FastAPI(title="Currency Converter API", description="A simple API to convert currencies using exchange rates from open.er-api.com", version="1.0.0")


@app.get("/")
def home():
    return {"message": "Currency Converter API is running successfully!!!"}

@app.get("/rates/{base}")
def rates(base: str):
    all_rates = get_exchange_rate(base)
    if all_rates is None:
        raise HTTPException(status_code=404, detail="Currency rates not found")
    return {"base": base.upper(), "rates": rates}

@app.get("/convert", response_model=ConversionResponse)
def convert_currency(amount: float, from_currency: str, to_currency: str):
    if amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be greater than 0")
    answer = convert(amount, from_currency, to_currency)
    if answer is None:
        raise HTTPException(status_code=404, detail="Invalid currency or rates unavailable")
    
    rate, result = answer
    return ConversionResponse(
        from_currency=from_currency.upper(),
        to_currency=to_currency.upper(),
        amount=amount,
        rate=rate,
        result=result
    )   