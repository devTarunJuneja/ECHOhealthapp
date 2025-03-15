import streamlit as st
import time
import requests
import datetime
import json
from streamlit_extras.colored_header import colored_header
from streamlit_calendar import calendar

# ------------------------------
# Page & API Setup
# ------------------------------
st.set_page_config(page_title="EchoHealth - Prescription Management", layout="wide")

# ------------------------------
# Embed Your API Key Here (Note: This is insecure in production!)
# ------------------------------
API_KEY = "AIzaSyAR7GyNlIjaGi6Q5Ea-J9y4XBQ4TaxIcDg"

# ------------------------------
# Enhanced CSS for Modern, Polished UI
# ------------------------------
st.markdown("""
<style>
/* Gradient background for the entire page */
body {
    background: linear-gradient(to bottom right, #fff, #ffeef3);
    font-family: Arial, sans-serif;
    color: #333;
    margin: 0;
    padding: 0;
}
/* Headings */
h1, h2, h3, h4 {
    color: #e75480;
    text-align: center;
    margin-bottom: 0.5rem;
}
/* Section Container */
.section {
    padding: 20px;
    margin-bottom: 20px;
    background-color: #ffffffcc; /* Subtle white overlay */
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
}
/* Boxes for appointments, prescriptions, doctors */
.appointment-box, .prescription-box, .doctor-box {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
    background-color: #fafafa;
}
/* Dashboard Container with subtle gradient & shadow */
.dashboard-container {
    background: linear-gradient(135deg, #fff 0%, #ffeef3 100%);
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}
/* Reading Card */
.reading-card {
    background-color: #ffffff;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    margin-bottom: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    display: flex;
    align-items: center;
}
.reading-card-icon {
    font-size: 1.5rem;
    margin-right: 10px;
    color: #e75480;
}
.reading-card h4 {
    margin: 0 0 0.5rem 0;
    color: #e75480;
    font-weight: 600;
    text-align: left;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# Dummy Data
# ------------------------------
doctor_appointments = [
    {"doctor": "Dr. John Smith (ENT Specialist)", "date": "2025-03-15", "time": "10:00 AM", "status": "Confirmed"},
    {"doctor": "Dr. Sarah Johnson (Speech Therapist)", "date": "2025-03-20", "time": "02:30 PM", "status": "Pending"},
    {"doctor": "Dr. Michael Lee (Laryngologist)", "date": "2025-03-25", "time": "01:00 PM", "status": "Confirmed"},
]

prescriptions = {
    "Dr. John Smith (ENT Specialist)": [
        "Gargle with warm salt water", 
        "Take anti-inflammatory medication", 
        "Avoid shouting"
    ],
    "Dr. Sarah Johnson (Speech Therapist)": [
        "Daily vocal warm-ups", 
        "Breathing exercises", 
        "Hydrate frequently"
    ],
    "Dr. Michael Lee (Laryngologist)": [
        "Use a humidifier", 
        "Reduce caffeine intake", 
        "Perform resonance therapy"
    ],
}

# ------------------------------
# AI Functions (Gemini API)
# ------------------------------
def get_prescription_recommendation(symptoms):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": f"Suggest a prescription for these symptoms: {symptoms}"}]
        }]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "⚠️ Error fetching prescription recommendations. Please try again later."

def find_doctor(query):
    """
    Uses the Gemini API to search for doctors.
    The prompt instructs the API to output a JSON array of doctor objects.
    Each object includes 'id', 'name', 'specialty', 'contact', and 'bio'.
    """
    prompt = (
        f"Return a JSON array of doctor objects that match the following query: {query}. "
        "Each object should have the keys: id, name, specialty, contact, and bio. "
        "If no doctor is found, return an empty array."
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        try:
            results = json.loads(text)
            return results if isinstance(results, list) else []
        except json.JSONDecodeError:
            # Fallback: return the raw text as a single doctor entry
            return [{"id": "n/a", "name": text, "specialty": "N/A", "contact": "N/A", "bio": "N/A"}]
    else:
        return [{"id": "n/a", "name": "Error", "specialty": "", "contact": "", "bio": "Error fetching data from Gemini API"}]

def get_doctor_details(doctor_id, doctor_name):
    """
    Uses the Gemini API to fetch detailed information about a doctor.
    The prompt instructs the API to return a JSON object with keys: bio, experience, education, and contact.
    """
    prompt = (
        f"Provide detailed information about Dr. {doctor_name} in JSON format. "
        "The JSON object should include the keys: bio, experience, education, and contact."
    )
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": prompt}]}]}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        text = response.json()["candidates"][0]["content"]["parts"][0]["text"]
        try:
            details = json.loads(text)
            return details
        except json.JSONDecodeError:
            return {"bio": text, "experience": "N/A", "education": "N/A", "contact": "N/A"}
    else:
        return {"bio": "Error fetching data from Gemini API", "experience": "", "education": "", "contact": ""}

# ------------------------------
# Page Title
# ------------------------------
st.markdown("<h1>🏥 Prescription Management</h1>", unsafe_allow_html=True)
st.markdown("<h4>Manage your voice health with AI-powered prescriptions and doctor appointments.</h4>", unsafe_allow_html=True)

# ------------------------------
# Appointment Scheduler
# ------------------------------
colored_header(
    label="📅 Schedule an Appointment",
    description="Book a consultation with a specialist.",
    color_name="blue-70"
)
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("**🩺 Choose a Doctor**")
doctor_choice = st.selectbox("Select a doctor", [doc["doctor"] for doc in doctor_appointments])
st.markdown("**📆 Choose a Date & Time**")
appointment_date = st.date_input("Select a date")
appointment_time = st.time_input("Select a time")
if st.button("📌 Book Appointment"):
    st.success(f"✅ Appointment with {doctor_choice} booked for {appointment_date} at {appointment_time}")
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Find a Doctor
# ------------------------------
colored_header(
    label="🔍 Find a Doctor",
    description="Search for doctors by name or specialty.",
    color_name="green-70"
)
st.markdown("<div class='section'>", unsafe_allow_html=True)
search_query = st.text_input("Enter doctor's name or specialty")
if st.button("Search"):
    with st.spinner("Searching for doctors..."):
        results = find_doctor(search_query)
        if results:
            for doctor in results:
                st.markdown(
                    f"<div class='doctor-box'><strong>Name:</strong> {doctor['name']}<br>"
                    f"<strong>Specialty:</strong> {doctor['specialty']}<br>"
                    f"<strong>Contact:</strong> {doctor['contact']}</div>", 
                    unsafe_allow_html=True
                )
                if st.button(f"View Details - {doctor['name']}", key=doctor.get('id', doctor['name'])):
                    details = get_doctor_details(doctor.get('id', "n/a"), doctor['name'])
                    st.markdown(
                        f"**Details:**<br>Bio: {details.get('bio')}<br>"
                        f"Experience: {details.get('experience')}<br>"
                        f"Education: {details.get('education')}<br>"
                        f"Contact: {details.get('contact')}",
                        unsafe_allow_html=True
                    )
        else:
            st.error("No doctors found.")
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# AI-Powered Prescription Suggestion
# ------------------------------
colored_header(
    label="💊 AI-Powered Prescription Suggestion",
    description="Get medication and therapy recommendations.",
    color_name="red-70"
)
st.markdown("<div class='section'>", unsafe_allow_html=True)
symptoms = st.text_area("📝 Describe your symptoms (e.g., sore throat, hoarseness, difficulty speaking)")
if st.button("🤖 Get AI Prescription"):
    with st.spinner("Fetching AI recommendation..."):
        time.sleep(1.5)
        prescription_suggestion = get_prescription_recommendation(symptoms)
        st.success("✅ Prescription recommendation generated!")
        st.markdown(
            f"<div style='padding:10px; border-radius:5px; background-color:#fff0f5; color:#333; border:1px solid #f8c8d0;'>{prescription_suggestion}</div>", 
            unsafe_allow_html=True
        )
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# View Current Prescriptions
# ------------------------------
colored_header(
    label="📋 Your Prescriptions",
    description="View doctor-prescribed treatments and medications.",
    color_name="gray-70"
)
st.markdown("<div class='section'>", unsafe_allow_html=True)
selected_doctor = st.selectbox("🩺 Select a doctor to view prescriptions", list(prescriptions.keys()))
st.markdown("### 📜 Prescriptions:")
for item in prescriptions[selected_doctor]:
    st.markdown(f"<div class='prescription-box'>✅ {item}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Voice Health Dashboard
# ------------------------------
colored_header(
    label="📊 Voice Health Dashboard",
    description="Showcasing your progress and upcoming schedule.",
    color_name="blue-70"
)

st.markdown("<div class='dashboard-container'>", unsafe_allow_html=True)

# Row of progress bars (two-column layout)
progress_data = {
    "Daily Vocal Warm-ups": 80,
    "Hydration Level": 90,
    "Medication Adherence": 75,
    "Breathing Exercises": 60,
}
progress_items = list(progress_data.items())

col1, col2 = st.columns(2)
icons = ["🎤", "💧", "💊", "🫁"]  # Example icons for each reading

for i in range(0, len(progress_items), 2):
    idx_icon1 = i % len(icons)
    key1, val1 = progress_items[i]
    with col1:
        st.markdown("<div class='reading-card'>", unsafe_allow_html=True)
        st.markdown(f"<span class='reading-card-icon'>{icons[idx_icon1]}</span>", unsafe_allow_html=True)
        st.markdown(f"<h4>{key1}</h4>", unsafe_allow_html=True)
        st.progress(val1 / 100)
        st.markdown("</div>", unsafe_allow_html=True)
    
    if i + 1 < len(progress_items):
        idx_icon2 = (i+1) % len(icons)
        key2, val2 = progress_items[i + 1]
        with col2:
            st.markdown("<div class='reading-card'>", unsafe_allow_html=True)
            st.markdown(f"<span class='reading-card-icon'>{icons[idx_icon2]}</span>", unsafe_allow_html=True)
            st.markdown(f"<h4>{key2}</h4>", unsafe_allow_html=True)
            st.progress(val2 / 100)
            st.markdown("</div>", unsafe_allow_html=True)

# Health Calendar
st.markdown("<h3 style='text-align:left; margin-top:40px;'>Health Calendar</h3>", unsafe_allow_html=True)
calendar(events=[
    {"title": "Appointment - Dr. John Smith", "date": "2025-03-15"},
    {"title": "Medication - Gargle with Salt Water", "date": "2025-03-16"},
    {"title": "Appointment - Dr. Sarah Johnson", "date": "2025-03-20"},
    {"title": "Therapy - Resonance Training", "date": "2025-03-22"},
])
st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------
# Footer
# ------------------------------

st.markdown("<p style='text-align: center; color: #888;'>🔊 Powered by EchoHealth Prescription System</p>", unsafe_allow_html=True)
