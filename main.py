import requests
from tkinter import messagebox
from dotenv import load_dotenv
import os
import streamlit as st

# load env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Set page configuration
st.set_page_config(page_title="Weather App", page_icon=":partly_sunny:")

# Custom CSS styles
with open('css\styling.css') as f:
    css = f.read()
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Streamlit
st.write("Weather App")
st.write("This app is built using Streamlit and Python")

city = st.text_input("","",placeholder="Enter city name")
col1, col2 = st.columns([.25,1])

with col1:
    button = st.button("Get Weather")
with col2:   
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
if clear:
    st.session_state.clear()