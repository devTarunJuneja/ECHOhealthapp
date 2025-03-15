import streamlit as st
import requests
import os

# ------------------------------
# Page & CSS Setup
# ------------------------------
st.set_page_config(page_title="AudiBuddy - Voice Health Chatbot", layout="wide")

# Inline CSS for enhanced UI design
st.markdown("""
    <style>
    /* Overall body background */
    body {
        background-color: #f5f5f5;
    }
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-image: linear-gradient(#4e54c8, #8f94fb);
        color: white;
    }
    /* Chat container styling */
    .chat-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    /* Chat bubble styles */
    .user-msg {
        text-align: right;
        background-color: #DCF8C6;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        display: inline-block;
        max-width: 70%;
    }
    .bot-msg {
        text-align: left;
        background-color: #E6E6E6;
        padding: 10px 15px;
        border-radius: 15px;
        margin: 8px 0;
        display: inline-block;
        max-width: 70%;
    }
    /* Predefined question buttons */
    .predefined-btn {
        margin: 5px;
        border-radius: 10px;
        padding: 10px 15px;
        background-color: #4e54c8;
        color: white;
        border: none;
        cursor: pointer;
    }
    .predefined-btn:hover {
        background-color: #3b40a4;
    }
    </style>
    """, unsafe_allow_html=True)


def get_gemini_response(user_input):
    API_KEY = os.getenv("GEMINI_API_KEY")  # Securely stored in your .env file
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAR7GyNlIjaGi6Q5Ea-J9y4XBQ4TaxIcDg"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json().get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response from API.")
    else:
        return "⚠️ Error: Unable to fetch response. Please try again later."

# ------------------------------
# Session State for conversation history
# ------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ------------------------------
# Main Chatbot UI
# ------------------------------
st.title("🤖 AudiBuddy")
st.markdown("👋 **Welcome! Ask me about your voice health.**")

# Predefined Questions Section
st.markdown("### Mostly Asked Questions")
col1, col2 = st.columns(2)
predefined_questions = [
    "How can I improve my voice health?",
    "What are common symptoms of voice disorders?",
    "Can you analyze my voice sample?",
    "What are tips for clear speech?"
]

# Display buttons in two columns
for idx, question in enumerate(predefined_questions):
    if idx % 2 == 0:
        with col1:
            if st.button(question, key=f"pre_{idx}", help="Click to ask this question"):
                st.session_state.chat_history.append({"role": "user", "message": question})
                response = get_gemini_response(question)
                st.session_state.chat_history.append({"role": "bot", "message": response})
    else:
        with col2:
            if st.button(question, key=f"pre_{idx}", help="Click to ask this question"):
                st.session_state.chat_history.append({"role": "user", "message": question})
                response = get_gemini_response(question)
                st.session_state.chat_history.append({"role": "bot", "message": response})

# Chat History Display
st.markdown("### Conversation")
chat_container = st.container()
with chat_container:
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(f'<div class="user-msg">{chat["message"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">{chat["message"]}</div>', unsafe_allow_html=True)

# ------------------------------
# User Input Area with Form
# ------------------------------
with st.form("chat_input", clear_on_submit=True):
    user_input = st.text_input("Ask about your voice health...", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        st.session_state.chat_history.append({"role": "user", "message": user_input})
        response = get_gemini_response(user_input)
        st.session_state.chat_history.append({"role": "bot", "message": response})
