from fastapi import FastAPI
from app.routes import auth, news, weather

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(news.router, prefix="/news", tags=["news"])
app.include_router(weather.router, prefix="/weather", tags=["weather"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the DataHat Backend API"}