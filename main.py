import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os
import streamlit as st


# load env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# get CURRENT weather data
url = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=London" + "&aqi=yes"
response = requests.get(url)

st.write("Weather App")
st.write("This app is built using Streamlit and Python")
st.write("City: " + response.json()["location"]["name"])
st.write("Region: " + response.json()["location"]["region"])
st.write("Country: " + response.json()["location"]["country"])
st.write("Local Time: " + response.json()["location"]["localtime"])
st.write("Temperature: " + str(response.json()["current"]["temp_c"]) + "°C")


