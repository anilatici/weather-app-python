import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os
import streamlit as st

# load env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Streamlit
st.write("Weather App")
st.write("This app is built using Streamlit and Python")

city = st.text_input("Enter a city name", "")
button = st.button("Get Weather")
clear = st.button("Clear")

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
            st.write("Current Weather in " + city)
            st.write("Temperature: " + str(data["current"]["temp_c"]) + "°C")
            st.write("Condition: " + data["current"]["condition"]["text"])
            st.write("Wind: " + str(data["current"]["wind_kph"]) + " km/h")
            st.write("Humidity: " + str(data["current"]["humidity"]) + "%")
    else:
        data = response.json()
        if "error" in data:
            st.write("Error: " + str(response.status_code))
            st.write(data["error"]["message"])