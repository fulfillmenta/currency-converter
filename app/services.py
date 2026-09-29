import time
import requests

cache = {}
CACHE_EXPIRATION = 3600

def get_exchange_rate(base):
    base = base.upper()

    if base in cache:
        saved = cache[base]
        age = time.time() - saved['time']
        if age < CACHE_EXPIRATION:
            return saved['rates']

    url = "https://open.er-api.com/v6/latest/" + base
    try:
        response = requests.get(url, timeout = 10)
        data = response.json()
    except Exception:
        return None

    if data.get("result") != "success":
        return None

    cache[base] = {"time": time.time(), "rates": data["rates"]}
    return data["rates"]

def convert(amount, from_currency, to_currency):
    rates = get_exchange_rate(from_currency)
    if rates is None:
        return None

    to_currency = to_currency.upper()
    if to_currency not in rates:
        return None

    rates = rates[to_currency]
    result = round(amount * rates, 2)
    return rates, result