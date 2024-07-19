import pandas as pd
from retry_requests import retry

import requests_cache
import openmeteo_requests

# Функция определения широты и долготы по названию города
def coordinates(name_sity): 
    lat = -1 # широта
    lon = -1 # долгота   
      
    try:
        df = pd.read_csv("russian_towns.tsv", sep="\t")

        for i in enumerate(df['name']):
            if name_sity.lower() == i[1].lower():
                lat = df.iloc[i[0]]['lat']
                lon = df.iloc[i[0]]['lon']      
                return (lat, lon)
            
        for i in enumerate(df['alternative_names']):
            for j in enumerate(i[1].split(',')):                
                if  name_sity.lower() == j[1].lower():
                    lat = df.iloc[i[0]]['lat']
                    lon = df.iloc[i[0]]['lon']      
                    return (lat, lon)         
    except Exception as e: 
        print(e)

    return (lat, lon)


# Функция предсказания погоды на ближайшее время
def func_weather(arg):
    
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    coord = coordinates(arg)     
    
    if coord[0] != -1 and coord[1] !=-1:
        params = {
            "latitude": coord[0],
            "longitude": coord[1],
            "hourly": ["temperature_2m", 'relative_humidity_2m', 'wind_speed_10m', 'precipitation_probability'], # cписок погодных переменных, которые должны быть возвращены        
            "forecast_days": 1 # прогноз на 1 день
        }
        responses = openmeteo.weather_api(url, params=params)
        
        # Process first location. Add a for-loop for multiple locations or weather models
        response = responses[0]
                
        # Process hourly data. The order of variables needs to be the same as requested.
        hourly = response.Hourly()
        
        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()
        hourly_wind_speed_10m = hourly.Variables(2).ValuesAsNumpy()
        hourly_precipitation_probability = hourly.Variables(3).ValuesAsNumpy()            

        temp = str(round(hourly_temperature_2m[0],2)) # температура
        humidity = str(hourly_relative_humidity_2m[0]) # влажность воздуха
        wind = str(round(hourly_wind_speed_10m[0],2)) # скорость ветра
        proba = str(hourly_precipitation_probability[0]) # вероятность выпадения осадков            
        
        return (f"Температура воздуха: {temp} градусов С", f"Относительная влажность: {humidity} %", f"Скорость ветра: {wind} м/с", f"Вероятность выпадения осадков: {proba} %")
    else:
        return (f"Город не найден", f" ", f" ", f" ")