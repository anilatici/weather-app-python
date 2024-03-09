import requests
import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
import os
import streamlit as st
import json


# load env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


# get CURRENT weather data
url = "http://api.weatherapi.com/v1/current.json?key=" + API_KEY + "&q=London" + "&aqi=yes"
response = requests.get(url)

st.write("Weather App")
st.write("This app is built using Streamlit and Python")
