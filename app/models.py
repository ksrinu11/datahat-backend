from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class NewsRequest(BaseModel):
    query: str

class WeatherRequest(BaseModel):
    city: str