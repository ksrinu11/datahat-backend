# DataHat Backend API

This is a FastAPI-based backend that includes:
- ✅ Authentication (login with hardcoded credentials)
- ✅ News Headlines using NewsAPI
- ✅ Weather Forecast using WeatherAPI

## 📦 Installation

```bash
git clone <repo-url>
cd datahat_backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Running the API

```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## 🔐 Authentication

- Username: `admin`
- Password: `admin123`

## 🔑 Environment Variables

Create a `.env` file and add your keys based on `.env.example`.

## 📬 APIs Used

- NewsAPI: [https://newsapi.org/](https://newsapi.org/)
- WeatherAPI: [https://www.weatherapi.com/](https://www.weatherapi.com/)