import streamlit as st
import time
import requests
import os
import datetime

# Set up page title and layout
st.set_page_config(page_title="EchoHealth - Voice Exercises", layout="wide")

# Minimal custom CSS for a clean white/light pink theme and enlarged video display
st.markdown("""
<style>
body {
    background-color: #ffffff;
    font-family: Arial, sans-serif;
    color: #333;
}
h1, h2, h3, h4 {
    color: #e75480;
    text-align: center;
}
.video-container {
    display: flex;
    justify-content: center;
    margin: 20px 0;
}
.video-container iframe {
    width: 800px;
    height: 450px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# Load API key securely
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize session state for progress tracking
if "exercise_points" not in st.session_state:
    st.session_state["exercise_points"] = 0
if "exercise_progress" not in st.session_state:
    st.session_state["exercise_progress"] = {}
if "exercise_streak" not in st.session_state:
    st.session_state["exercise_streak"] = 0
if "last_exercise_date" not in st.session_state:
    st.session_state["last_exercise_date"] = None
if "user_level" not in st.session_state:
    st.session_state["user_level"] = 1

# Exercise data
exercise_types = {
    "🫁 Breathing Techniques": "Improve breath control and lung capacity for better vocal support.",
    "🎵 Vocal Warm-ups": "Gently prepare your vocal cords to prevent strain and improve clarity.",
    "🏋️ Strengthening Exercises": "Enhance vocal endurance and stability for longer speaking sessions.",
    "📢 Speech Clarity Training": "Boost articulation and resonance for clearer speech.",
    "🎶 Resonance Therapy": "Improve voice projection and tone balance for a healthier voice."
}

exercise_videos = {
    "🫁 Breathing Techniques": "https://youtu.be/_Y5SNjo6OGs?si=zDiCnBAz7sL9LeSo",  
    "🎵 Vocal Warm-ups": "https://youtu.be/UWRucBanDF0?si=b7bSxqBXBQjMwBJZ",  
    "🏋️ Strengthening Exercises": "https://youtu.be/xjXJaeBWRpU?si=KKG0k7NDTeJ3ZzPU",  
    "📢 Speech Clarity Training": "https://youtu.be/UHqxDZVlUbY?si=KnRl58-TcHAKqmMJ",  
    "🎶 Resonance Therapy": "https://youtu.be/Jk-ItSzlRjI?si=NF8rjWxAF19g8t0n"  
}

def get_exercise_recommendation(query):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAR7GyNlIjaGi6Q5Ea-J9y4XBQ4TaxIcDg"
    headers = {"Content-Type": "application/json"}
    data = {"contents": [{"parts": [{"text": query}]}]}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return "⚠️ Error fetching exercise recommendations. Please try again later."

# Page title and introduction
st.markdown("<h1>🏋️ Voice Therapy Exercises</h1>", unsafe_allow_html=True)
st.markdown("<h4>Strengthen your voice with these scientifically-backed exercises.</h4>", unsafe_allow_html=True)

# Exercise category selection
st.markdown("### Select an Exercise Category")
selected_exercise = st.selectbox("Choose an exercise type", list(exercise_types.keys()))
st.markdown(f"**About:** {exercise_types[selected_exercise]}")

# Display enlarged video
st.markdown("### Exercise Demo")
with st.container():
    st.markdown("<div class='video-container'>", unsafe_allow_html=True)
    st.video(exercise_videos[selected_exercise])
    st.markdown("</div>", unsafe_allow_html=True)

# Guidance button appears right after video
st.markdown("### Need Guidance?")
if st.button("🧑‍⚕️ Get Step-by-Step Guide"):
    with st.spinner("Fetching exercise guide..."):
        time.sleep(1.5)
        query = f"Provide step-by-step instructions for {selected_exercise.lower()}."
        guide = get_exercise_recommendation(query)
        st.success("Exercise guide generated!")
        st.markdown(guide)

# Progress Tracker Section
st.markdown("### Your Progress")
today = datetime.date.today()
if st.session_state["last_exercise_date"] != today:
    st.session_state["exercise_streak"] += 1
    st.session_state["last_exercise_date"] = today

st.write(f"**Daily Streak:** {st.session_state['exercise_streak']} days")
st.write(f"**Total Points:** {st.session_state['exercise_points']} points")
st.write(f"**Level:** {st.session_state['user_level']}")
progress_percentage = min(st.session_state["exercise_points"] / 100, 1.0)
st.progress(progress_percentage)

# Checkbox to mark exercise as completed
exercise_complete = st.checkbox(f"Mark {selected_exercise} as Completed")
if exercise_complete and selected_exercise not in st.session_state["exercise_progress"]:
    st.session_state["exercise_progress"][selected_exercise] = True
    st.session_state["exercise_points"] += 10
    st.session_state["user_level"] = 1 + st.session_state["exercise_points"] // 100
    st.success(f"You earned 10 points for completing {selected_exercise}!")


if len(st.session_state["exercise_progress"]) >= 3:
    st.success("🔥 Amazing! You're consistently improving your voice. Keep going!")
elif len(st.session_state["exercise_progress"]) >= 1:
    st.info("💪 Good start! Try to complete more exercises.")
else:
    st.warning("🚀 Start your first exercise to earn points!")

# Leaderboard section
st.markdown("### Leaderboard")
leaderboard = [
    {"name": "Tarun J.", "avatar": "🦸", "points": 50},
    {"name": "Alex K.", "avatar": "🧑‍🚀", "points": 40},
    {"name": "Sophia M.", "avatar": "👩‍🎤", "points": 30},
    {"name": "You", "avatar": "🦾", "points": st.session_state["exercise_points"]}
]
leaderboard = sorted(leaderboard, key=lambda x: x["points"], reverse=True)
for i, user in enumerate(leaderboard, start=1):
    st.write(f"**{i}. {user['avatar']} {user['name']}** - {user['points']} pts")

# Footer

st.markdown("<p style='text-align: center; color: #888;'>Powered by EchoHealth Voice Therapy</p>", unsafe_allow_html=True)
