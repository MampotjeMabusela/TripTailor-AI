from fastapi import FastAPI, Request
from itinerary_builder import build_itinerary
from pricing_predictor import predict_price
from risk_alerts import get_weather_alerts, get_geopolitical_alerts
from crm_integration import update_customer_profile

app = FastAPI()

@app.post("/generate-itinerary")
async def generate_itinerary(request: Request):
    data = await request.json()
    itinerary = build_itinerary(data["prompt"])
    update_customer_profile(data["customer_id"], itinerary)
    return {"itinerary": itinerary}

@app.post("/predict-price")
async def price_prediction(request: Request):
    data = await request.json()
    price = predict_price(data)
    return {"predicted_price": float(price[0])}

@app.get("/risk-alerts/{location}")
def risk_alerts(location: str):
    weather = get_weather_alerts(location)
    geo = get_geopolitical_alerts(location)
    return {"weather": weather, "geopolitical": geo}
