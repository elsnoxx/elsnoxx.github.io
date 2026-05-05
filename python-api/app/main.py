from http.client import HTTPException
from fastapi import FastAPI
from evaluation import evaluate_stock

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/evaluate/{ticker_symbol}")
def evaluate_stock_endpoint(ticker_symbol: str):
    evaluation = evaluate_stock(ticker_symbol)
    if evaluation is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return {"ticker": ticker_symbol, "evaluation": evaluation}