import requests
from config import WORLD_WEATHER_API_KEY

def weather_by_city(city_name: str):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key" : WORLD_WEATHER_API_KEY,
        "q" : city_name,
        "format" : "json",
        "num_of_days" : "1",
        "lang" : "ru"
    }
    response = requests.get(weather_url, params=params).json()
    if "data" in response:
        if "current_condition" in response["data"]:
            try:
                return response["data"]["current_condition"][0]
            except(IndexError, TypeError):
                return False    
    return False

    
if __name__ == "__main__":
    print(weather_by_city("Vyborg"))