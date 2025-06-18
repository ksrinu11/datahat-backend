from fastapi import APIRouter
from app.models import NewsRequest
import requests

router = APIRouter()

NEWS_API_KEY = "6303cff7a4d942fdb64a8ebc74860f99"

@router.post("/headlines")
def get_news(news_req: NewsRequest):
    url = f"https://newsapi.org/v2/everything?q={news_req.query}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    return response.json()