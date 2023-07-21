import datetime as dt
import requests
import json
from win10toast import ToastNotifier
import time

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'cf194c4ba346e9344c35914e2f2767a4'
CITY = "Xixon"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

def display_weather_notification():
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()

    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
    feels_like_kelvin = response['main']['temp']
    feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
    wind_speed = response['wind']['speed']
    humdity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    toast = ToastNotifier()
    toast.show_toast(f"Weather in {CITY}",
                     f"Temperature: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F\n"
                     f"Feels Like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F\n"
                     f"Humidity: {humdity}%\n"
                     f"Windspeed: {wind_speed} mph\n"
                     f"Description: {description}\n"
                     f"Sunrise: {sunrise_time}\n"
                     f"Sunset: {sunset_time}",
                     duration=10)

while True:
    display_weather_notification()
    time.sleep(1) 