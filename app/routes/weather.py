from fastapi import APIRouter
from app.models import WeatherRequest
import requests
import os

router = APIRouter()

WEATHER_API_KEY = "80577dfa5a36410392c200149251806"

@router.post("/")
def get_weather(weather_req: WeatherRequest):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={weather_req.city}"
    response = requests.get(url)
    return response.json()