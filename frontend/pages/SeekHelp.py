import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import requests

# ✅ **Google Maps API Key**
GOOGLE_MAPS_API_KEY = "AIzaSyAR7GyNlIjaGi6Q5Ea-J9y4XBQ4TaxIcDg"

# 🔷 **Streamlit Page Config**
st.set_page_config(page_title="Seek Help - EchoHealth", layout="wide")

# 📌 **Page Title**
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏥 Seek Medical Help</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Find the nearest ENT specialists for voice-related treatment.</h4>", unsafe_allow_html=True)

# 📍 **List of Verified ENT Doctors in Ambala & MMDU Mullana**
doctors = [
    {"name": "Dr. Harpuneet Kaur", "address": "Sidak E.N.T Care, Model Town, Ambala City", "lat": 30.3753, "lon": 76.7821},
    {"name": "Dr. Sandeep Inder Singh Cheema", "address": "Leelawati ENT, Ambala City", "lat": 30.3782, "lon": 76.7756},
    {"name": "Dr. Rishi Gautam Aggarwal", "address": "Sri Onkar Eye & ENT Care Centre, Ambala", "lat": 30.3761, "lon": 76.7805},
    {"name": "Dr. Harpreet Singh", "address": "Park Hospital, Ambala", "lat": 30.3728, "lon": 76.7752},
    {"name": "Dr. Krishan Kudawla", "address": "SARVOTTAM ENT CLINIC, Ambala Cantt", "lat": 30.3396, "lon": 76.8181},
    {"name": "Dr. Vijay Bansal", "address": "Rotary Ambala Cancer & General Hospital, Ambala Cantt", "lat": 30.3372, "lon": 76.8184},
    {"name": "Dr. Rajesh Kumar", "address": "MMDU Mullana ENT Dept., Mullana", "lat": 30.2594, "lon": 77.0459},
    {"name": "Dr. Sunil Verma", "address": "Maharishi Markandeshwar Hospital, Mullana", "lat": 30.2589, "lon": 77.0465},
    {"name": "Dr. Anjali Sharma", "address": "ENT & Speech Therapy, MMDU Mullana", "lat": 30.2601, "lon": 77.0448},
    {"name": "Dr. Pankaj Gupta", "address": "Voice & Hearing Clinic, MMDU Mullana", "lat": 30.2597, "lon": 77.0472},
]

# ✅ **User Location Selection**
st.markdown("### 📍 Select Your Location")
location_query = st.text_input("Enter your city or area:", placeholder="E.g., Ambala, Mullana")

# Function to Get Coordinates from Address (Google Maps API)
def get_coordinates(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={GOOGLE_MAPS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
    return None, None

# Get Coordinates
user_lat, user_lon = get_coordinates(location_query) if location_query else (30.3753, 76.7821)  # Default to Ambala

# ✅ **Show Locations on Map**
st.markdown("---")
st.markdown("### 🌍 ENT Specialists on Map")

# **Create a Map Centered on User Location**
m = folium.Map(location=[user_lat, user_lon], zoom_start=13)

# **Add Markers for Each Doctor**
for doctor in doctors:
    folium.Marker(
        [doctor["lat"], doctor["lon"]],
        popup=f"<b>{doctor['name']}</b><br>{doctor['address']}",
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

# **User Location Marker**
if location_query:
    folium.Marker(
        [user_lat, user_lon],
        popup="<b>Your Location</b>",
        icon=folium.Icon(color="red", icon="home"),
    ).add_to(m)

# **Render Map in Streamlit**
folium_static(m, width=1000, height=600)


# **Footer**
st.markdown("---")
st.markdown("<p style='text-align: center; color: #888;'>🔊 Powered by EchoHealth</p>", unsafe_allow_html=True)
