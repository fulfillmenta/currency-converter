Currency Converter API

A simple FastAPI backend that converts between currencies using live exchange rates.

Live Demo

https://currency-converter-yg6g.onrender.com/docs

Note: this is hosted on Render's free tier. If it hasn't been used in a while, the first request may take 20-30 seconds to wake up.

Features

- Convert an amount from one currency to another
- View all exchange rates for a given base currency
- Rates are cached for 1 hour to avoid hitting the exchange rate API too often

Project Structure

currency-converter/
├── app/
│   ├── main.py        # FastAPI app and all endpoints
│   ├── models.py      # Pydantic request/response models
│   └── services.py    # Fetch rates, cache them, do the conversion
├── test.py             # Tests for the API and conversion logic
├── requirements.txt    # Python packages needed
└── README.md           # How to install and run

Setup (run locally)

1. Clone the repo:
   git clone https://github.com/fulfillmenta/currency-converter.git
   cd currency-converter

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install packages:
   pip install -r requirements.txt

Run

uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/docs

Endpoints

- GET /  
  Health check, confirms the API is running

- GET /rates/{base}  
  Returns all exchange rates for a base currency  
  Example: /rates/USD

- GET /convert?amount=100&from_currency=USD&to_currency=NGN  
  Converts an amount from one currency to another

Test
pytest test.py

Deployment

This project is deployed on Render:
- Build Command: pip install -r requirements.txt
- Start Command: uvicorn app.main:app --host 0.0.0.0 --port $PORT

Tech Used

- Python
- FastAPI
- Requests (to call the exchange rate API)
- Pytest (for tests)
- Render (for hosting)