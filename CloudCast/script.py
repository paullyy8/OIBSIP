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
    visibility = weather_info['visibility'] / 1000  # Convert from meters to kilometers    

    # Get precipitation data
    precipitation = weather_info.get('rain', {}).get('1h', 0)  # Rain volume in last hour (if available)
    precipitation_chance = "Low"  # Default value

    # Hypothetical precipitation chance logic
    if precipitation > 5:
        precipitation_chance = "High"
        chance_percent = 70  # Assume a high chance if there's significant rain
    elif 1 < precipitation <= 5:
        precipitation_chance = "Medium"
        chance_percent = 40  # Moderate chance for light rain
    else:
        precipitation_chance = "Low"
        chance_percent = 10  # Low chance if no rain is recorded

    # Formatted output in table format
    print("\n🌤️ Weather Information 🌤️")
    print("-" * 40)
    print(f"{'City':<20} : {user_input.capitalize()}")
    print(f"{'Weather':<20} : {weather}")
    print(f"{'Temperature':<20} : {temp}ºC")
    print(f"{'Feels Like':<20} : {feels_like}ºC")
    print("-" * 40)

    # Precipitation Details
    print("\n🌧️ Precipitation Details 🌧️")
    print("-" * 40)
    print(f"{'Precipitation Chances':<26} : {precipitation_chance} ({chance_percent}%)")
    print(f"{'Total Daily Volume':<20} : {precipitation} mm")  # Display precipitation in mm
    print("-" * 40)

    # Other Details
    print("\n📋 Other Details 📋")
    print("-" * 40)
    print(f"{'Humidity:':<20} : {humidity}%")
    print(f"{'Visibility:':<20} : {visibility} km")
    print("-" * 40)

    print("Thank you for using CloudCast! Have a great day!\n")