
---
<div align="center">
  <h1>CloudCast</h1>
</div>

## About the Project
CloudCast is a Command Line Based application designed to deliver accurate and up-to-date weather information. 

## Table of Contents
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Getting Started](#getting-started-with-CloudCast)
4. [Usage](#usage)
5. [Ending Note](#ending-note)

## Features
- **Real-Time Weather Updates**: Provides current weather data for specified locations.
- **Detailed Weather Information**: Includes the current weather condition, temperature, humidity.
- **Location-Based Search**: Fetches weather details based on city input.

## Technologies Used
- **Python**: Core programming language for the application logic.
- **Weather API**: To fetch real-time weather data.

Your instructions are a great start, but we can enhance them for clarity and a better user experience. Here’s a revised version that includes more context, step-by-step instructions, and additional tips for first-time users:

## Getting Started with CloudCast 🌤️
### 1. Clone the Repository
First, clone the CloudCast repository to your local machine:
```bash
git clone https://github.com/paullyy8/OIBSIP.git
cd OIBSIP/CloudCast
```

### 2. Install Required Packages
Next, navigate to the project directory and install the necessary packages:
```bash
pip install -r requirements.txt
```

### 3. Create an API Key
To fetch weather data, you need an API key from OpenWeatherMap:
- Go to [OpenWeatherMap](https://openweathermap.org/appid) and sign up for a free account.
- After logging in, generate your API key.

### 4. Store Your API Key Securely
Create a `.env` file in the project directory to store your API key securely. Add the following line to the `.env` file:
```
API_KEY=your_api_key_here
```
Make sure to replace `your_api_key_here` with your actual API key.

### 5. Ensure the `.env` File is Ignored
To prevent your API key from being shared, ensure that your `.env` file is included in the `.gitignore`.

### 6. Run the Application
Now you’re ready to run the CloudCast application! Use the following command:
```bash
python app.py
```

## Usage
1. **Enter a Location**: Type in the name of the city for which you want weather data.
2. **View Results**: Get real-time updates on temperature, humidity, and forecast.
3. **Explore Features**: Additional options for extended weather data and forecast.

## Ending Note
Whether it's sunshine or storms, stay prepared and informed with CloudCast at your side!

--- 
## 
<h3 align="center">Designed and Developed by <a href="https://bento.me/amit-paul">Amit Paul</a></h3>