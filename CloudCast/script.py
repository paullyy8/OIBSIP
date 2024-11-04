import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# Check if the API key is available and prompt the user if it's not
if not api_key:
    api_key = input("🚨 No API key found. Please enter your OpenWeatherMap API key: ")

# Welcome message
print("\nWelcome to CloudCast 🌥️!")
print("Get the latest weather information at your fingertips.\n")

# User input
user_input = input("Please enter the name of the city you'd like to check the weather for: ")

# Change units to 'metric' for Celsius
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

# Process the response
if weather_data.json()['cod'] == '404':
    print("\n🌧️ No city found. Please ensure you entered the correct city name.")
else:
    weather_info = weather_data.json()
    weather = weather_info['weather'][0]['main']
    temp = round(weather_info['main']['temp'])
    feels_like = round(weather_info['main']['feels_like'])
    humidity = weather_info['main']['humidity']

    # Formatted output
    print("\n🌤️ Weather Information 🌤️")
    print(f"City: {user_input.capitalize()}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}ºC")
    print(f"Feels Like: {feels_like}ºC")
    print(f"Humidity: {humidity}%\n")
    print("Thank you for using CloudCast! Have a great day! ☀️ \n")