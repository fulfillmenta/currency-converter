from enum import Enum
import requests
from pydantic import BaseModel


def fetch_currency_codes():
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD", timeout=10)
        data = response.json()
        if data.get("result") == "success":
            return sorted(data["rates"].keys())
    except Exception:
        pass

    return ["USD", "EUR", "GBP", "NGN", "JPY"]


CurrencyCode = Enum("CurrencyCode", {code: code for code in fetch_currency_codes()}, type=str)



class ConversionResponse(BaseModel):
    from_currency: str
    to_currency: str
    amount: float
    rate: float
    result: float