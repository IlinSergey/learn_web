import requests
from webapp.config import WORLD_WEATHER_API_KEY

def weather_by_city(city_name: str):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key" : WORLD_WEATHER_API_KEY,
        "q" : city_name,
        "format" : "json",
        "num_of_days" : "1",
        "lang" : "ru"
    }
    try:
        response = requests.get(weather_url, params=params)
        response.raise_for_status()
        weather = response.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        return False    
    return False