import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"The weather in {city} is {description} with {temperature}°C.")
else:
    print("City not found. Please check the name and try again.")

