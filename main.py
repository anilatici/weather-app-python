import os
import requests
from dotenv import load_dotenv
import streamlit as st

# load env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set page configuration
st.set_page_config(page_title="Weather App", page_icon=":partly_sunny:")

# use css
with open('css/styling.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Streamlit
st.write("Weather App")

# Text input for city
city = st.text_input("Enter city name")

# Buttons to trigger actions
col1, col2 = st.columns([.25, 1])
with col1:
    button = st.button("Get Weather")
with col2:
    clear = st.button("Clear")

# Define the directory where your local weather icons are stored
icons_dir = "weather_icons"

# get CURRENT weather data
if button:
    url = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=" + city + "&aqi=yes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            st.write("Error: " + str(response.status_code))
            st.write(data["error"]["message"])
        else:
            condition_icon_name = data["current"]["condition"]["icon"]
            # Determine if it's day or night
            is_day = data["current"]["is_day"]
            time_of_day = "day" if is_day else "night"
            condition_icon_path = icons_dir + "/" + time_of_day + "/" + condition_icon_name.split("/")[-1]
            st.write("Current Weather in ")
            characterCount = len(data["location"]["name"] + ", " + data["location"]["country"])
            if characterCount > 16:
                st.title(data["location"]["name"] + ", " + data["location"]["country"])
            elif characterCount > 10 and characterCount <= 16:
                st.title(data["location"]["name"] + ", " + data["location"]["country"])
            else:
                st.title(data["location"]["name"] + ", " + data["location"]["country"])
            st.image(condition_icon_path, width=100)
            temp_emoji = "🌡️" if data["current"]["temp_c"] > 15 else "❄️"
            st.write(temp_emoji + " Temperature: " + str(data["current"]["temp_c"]) + "°C")
            condition_emoji = "☀️" if is_day else "🌙"
            st.write(condition_emoji + " Condition: " + data["current"]["condition"]["text"])
            wind_emoji = "🌬️"
            st.write(wind_emoji + " Wind: " + str(data["current"]["wind_kph"]) + " km/h")
            humidity_emoji = "💧"
            st.write(humidity_emoji + " Humidity: " + str(data["current"]["humidity"]) + "%")
            
    else:
        data = response.json()
        if "error" in data:
            st.write("Error: " + str(response.status_code))
            st.write(data["error"]["message"])

# Clear session state if clear button is clicked
if clear:
    st.session_state.clear()
