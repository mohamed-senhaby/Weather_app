import requests 
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/headquarter-weather')
def get_headquarter_weather(include_maximum: Optional[bool] = False):
    params = {
        "latitude": 51.43,
        "longitude": 6.97,
        "current_weather": True,
        "timezone": "Europe/Berlin",
        "hourly": ["temperature_2m", "apparent_temperature"],
        "daily": ["temperature_2m_max", "apparent_temperature_max"]
    }

    end_ponit = "https://api.open-meteo.com/v1/dwd-icon"
    response = requests.get(url=end_ponit, params=params)

    weather = response.json()
    current_weather = weather["current_weather"]
    current_temperature = current_weather["temperature"]
    current_time = current_weather["time"]
    result = {
        "current_temperature": current_temperature,
        "current_time": current_time
    }
    if include_maximum:
        max_temperature = weather["daily"]["temperature_2m_max"][0]
        index_max_temp = weather["hourly"]["temperature_2m"].index(max_temperature)
        time = weather["hourly"]["time"][index_max_temp]
        apparent_temperature_max = weather["daily"]["apparent_temperature_max"][0]
        result.update({
            "max_temperature": max_temperature,
            "max_temperature_time": time,
            "max_apparent_temperature": apparent_temperature_max,
            "max_apparent_temperature_time": time
        })
    return result
