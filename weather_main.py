# https://medium.com/@tmango/plotting-geojson-files-with-matplotlib-5ed87df570ab
# https://www.weather.gov/documentation/services-web-api

from datetime import datetime, date
from ast import Raise
import requests
import json


def url_status(url):
    user_agent = {"sirch-corp.com": "sirchandistroix@gmail.com"}
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"URL loading error at: {url}")


def json_forecast(raw_data):
    properties = raw_data.get("properties")
    forecast = properties.get("forecast")
    return forecast


def json_hourly_forecast(raw_data):
    properties = raw_data.get("properties")
    fcHourly = properties.get("forecastHourly")
    return fcHourly


def datetime_formatter(dnt_string):
    return dnt_string.replace("T", " ")[:-12]
    

#####  #####  #####
#####  #####  #####

def get_weather():
    ### grab current date and time:
    raw_time = datetime.now()
    current_time = raw_time.strftime("%Y-%m-%d %H:%M:%S")

    ### weather.gov API only accepts up to 4 decimal places for coordinates (accuracy = within 30 meters)
    lat, lon = 41.4621, -87.16
    url = f"https://api.weather.gov/points/{lat},{lon}"
    raw_data = url_status(url)
    # seven_day_fc = json_forecast(raw_data)
    # print(url_status(seven_day_fc))

    hourly_fc = json_hourly_forecast(raw_data)
    hfc_data = requests.get(hourly_fc)
    hfc_formatted = hfc_data.json()
    periods = hfc_formatted.get("properties").get("periods")

    for p in periods:
        startTime = datetime_formatter(p.get("startTime"))
        ### = '2022-11-05 21'
        if startTime == current_time[:-6]:
            return p

'''
{'number': 1, 
'name': '', 
'startTime': '2022-10-31T16:00:00-05:00', 
'endTime': '2022-10-31T17:00:00-05:00', 
'isDaytime': True, 
'temperature': 56, 
'temperatureUnit': 'F', 
'temperatureTrend': None, 
'windSpeed': '5 mph', 
'windDirection': 'NNW', 
'icon': 'https://api.weather.gov/icons/land/day/rain_showers,60?size=large', 
'shortForecast': 'Rain Showers Likely', 
'detailedForecast': ''}
'''
