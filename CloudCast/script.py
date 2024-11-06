import os
from dotenv import load_dotenv
import requests
from datetime import datetime

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# Check if the API key is available and prompt the user if it's not
if not api_key:
    api_key = input("🚨 No API key found. Please enter your OpenWeatherMap API key: ")

# Welcome message
print("\nWelcome to CloudCast 🌥️!")

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
    weather = weather_info['weather'][0]['main']  # Main weather condition
    sky_condition = weather_info['weather'][0]['description']  # Sky condition
    temp = round(weather_info['main']['temp'])
    feels_like = round(weather_info['main']['feels_like'])
    humidity = weather_info['main']['humidity']
    visibility = weather_info['visibility'] / 1000  # Convert from meters to kilometers

    # Wind information
    wind_speed = round(weather_info['wind']['speed'])  # Wind speed in m/s
    wind_direction = weather_info['wind']['deg']  # Wind direction in degrees
    sunrise = weather_info['sys']['sunrise']  # Sunrise timestamp
    sunset = weather_info['sys']['sunset']  # Sunset timestamp

    # Convert timestamps to a readable format
    sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M')
    sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M')

    # Get precipitation data
    precipitation = weather_info.get('rain', {}).get('1h', 0)  # Rain volume in last hour (if available)
    precipitation_chance = "Low"  # Default value
    chance_percent = 0  # Initialize chance percentage

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

    # Display everything in a structured table format
    print("\n" + "=" * 80)
    print(f"{'Weather Information':^80}")
    print("=" * 80)

    print(f"{'City':<30} : {user_input.capitalize()}")
    print(f"{'Weather':<30} : {weather}")
    print(f"{'Sky Condition':<30} : {sky_condition.capitalize()}")
    print(f"{'Temperature':<30} : {temp}ºC")
    print(f"{'Feels Like':<30} : {feels_like}ºC")
    print(f"{'Sunrise':<30} : {sunrise_time}")
    print(f"{'Sunset':<30} : {sunset_time}")
    print("-" * 80)

    print(f"{'Precipitation Chances':<30} : {precipitation_chance} ({chance_percent}%)")
    print(f"{'Total Volume (last hour)':<30} : {precipitation} mm")
    print("-" * 80)

    print(f"{'Wind Speed':<30} : {wind_speed} m/s")
    print(f"{'Wind Direction':<30} : {wind_direction}°")
    print("-" * 80)

    print(f"{'Humidity':<30} : {humidity}%")
    print(f"{'Visibility':<30} : {visibility} km")
    print("=" * 80)

    print("\nThank you for using CloudCast! Have a great day!\n")