import streamlit as st
import base64

def get_base64_image(image_path):
    """Convert image to base64 format for embedding in HTML."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")



# Remove default Streamlit elements
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding-top: 0px !important; }  /* Removes extra padding */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

import os

# Get the absolute path of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the logo
logo_path = os.path.join(BASE_DIR, "C:/Users/HP/Desktop/ECHOhealth/assets/logo.jpeg")  # Adjust if needed

# Custom Compact Header
st.markdown(f"""
    <style>
        .header-container {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 8px 30px;
            background-color: white;
            border-bottom: 1px solid #f0f0f0;
        }}
        .logo-container {{
            display: flex;
            align-items: center;
        }}
        .logo-text {{
            font-size: 18px;
            font-weight: bold;
            color: #e91e63;
            margin-left: 8px;
        }}
        .login-button {{
            background-color: #e91e63;
            color: white;
            padding: 6px 16px;
            border-radius: 16px;
            font-size: 14px;
            font-weight: bold;
            text-decoration: none;
        }}
        .login-button:hover {{
            background-color: #d81b60;
        }}
    </style>
    <div class="header-container">
        <div class="logo-container">
            <img src="data:image/jpeg;base64,{logo_base64}" width="55">  <!-- Optimized logo size -->
            <span class="logo-text">EchoHealth</span>
        </div>
        <a href="#" class="login-button">Login</a>
    </div>
""", unsafe_allow_html=True)

# Hero Section Styling
st.markdown("""
    <style>
        .hero-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            background-image: linear-gradient(white, white), url('https://www.transparenttextures.com/patterns/cubes.png');
            background-size: cover;
            padding: 80px 20px;
        }
        .badge {
            background-color: #fce4ec;
            color: #e91e63;
            font-size: 14px;
            font-weight: bold;
            padding: 6px 12px;
            border-radius: 20px;
            display: inline-block;
            margin-bottom: 15px;
        }
        .badge span {
            background-color: #e91e63;
            color: white;
            font-size: 12px;
            padding: 4px 8px;
            border-radius: 10px;
            margin-left: 5px;
        }
        .hero-heading {
            font-size: 48px;
            font-weight: bold;
            color: black;
        }
        .hero-highlight {
            color: #e91e63;
        }
        .hero-subheading {
            font-size: 22px;
            color: #333;
            margin-top: 10px;
        }
        .hero-description {
            font-size: 16px;
            color: #555;
            max-width: 600px;
            margin-top: 10px;
        }
        .cta-button {
            background-color: #e91e63;
            color: white !important;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 24px;
            border-radius: 30px;
            text-decoration: none;
            margin-top: 20px;
            display: inline-block;
        }
        .cta-button:hover {
            background-color: #d81b60;
        }
    </style>
""", unsafe_allow_html=True)

# Hero Section Content
st.markdown("""
    <style>
        .button-container {
            margin-top: 20px;
        }
        .stButton>button {
            background-color: #e91e63 !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: bold !important;
            padding: 12px 24px !important;
            border-radius: 30px !important;
            border: none !important;
            cursor: pointer !important;
        }
        .stButton>button:hover {
            background-color: #d81b60 !important;
        }
    </style>
    
    <div class="hero-container">
        <div class="badge">
            ❤️ AI-Powered Voice Analysis <span>New</span>
        </div>
        <h1 class="hero-heading">Your Voice Deserves <span class="hero-highlight">Care</span></h1>
        <h2 class="hero-subheading">Advanced <span class="hero-highlight">Voice Pathology</span> Analysis & Exercises</h2>
        <p class="hero-description">
            Get accurate voice health reports and personalized vocal exercises to maintain and improve your vocal wellness.
        </p>
    </div>
""", unsafe_allow_html=True)

# Streamlit Button for Navigation
col1, col2, col3 = st.columns([2.8, 3, 1])
with col2:
    if st.button("Start Your Voice Journey", key="cta_button"):
        st.switch_page("pages/Diagnosis.py")  # Streamlit multipage navigation
# --- CSS for Section Layout & Styling ---
st.markdown("""
    <style>
        .section-title {
            font-size: 32px; /* Increased from 28px */
            font-weight: bold;
            color: black;
            display: flex;
            align-items: center;
        }
        .section-title-icon {
            color: #e91e63;
            font-size: 26px; /* Increased from 22px */
            margin-right: 10px;
        }

        /* List items */
        .list-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 15px;
        }
        .list-number {
            background-color: #fce4ec;
            color: #e91e63;
            font-size: 18px; /* Increased from 16px */
            font-weight: bold;
            width: 34px; /* Slightly bigger circle */
            height: 34px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 20px;
        }
        .list-content-title {
            font-size: 20px; /* Increased from 18px */
            font-weight: bold;
            color: black;
            margin-bottom: 3px;
        }
        .list-content-text {
            font-size: 16px; /* Increased from 14px */
            color: #555;
        }

        /* Dashboard image container */
        .dashboard-frame {
            background-color: white;
            border-radius: 15px;
            overflow: hidden;
            display: flex;
            justify-content: center;
            width: 100%;
            padding: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Create a Spacer Column (col0) + Larger Text Column (col1) + Image Column (col2) ---
# Adjust these ratios to taste:
#   0.3 => Left spacer
#   1.5 => Wider text column
#   1.0 => Image column
col0, col1, col2 = st.columns([0.1, 1.5, 1.0])

with col1:
    st.markdown("""
        <h2 class="section-title">
            <span class="section-title-icon">❗</span> Why Voice Health Matters
        </h2>
        <div class="list-item">
            <div class="list-number">1</div>
            <div>
                <div class="list-content-title">Early Detection</div>
                <div class="list-content-text">
                    Identify potential voice disorders before they become serious issues.
                </div>
            </div>
        </div>
        <div class="list-item">
            <div class="list-number">2</div>
            <div>
                <div class="list-content-title">Professional Performance</div>
                <div class="list-content-text">
                    Essential for speakers, singers, and professionals who rely on their voice.
                </div>
            </div>
        </div>
        <div class="list-item">
            <div class="list-number">3</div>
            <div>
                <div class="list-content-title">Overall Wellness</div>
                <div class="list-content-text">
                    Voice health is connected to physical and emotional well-being.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Dashboard image in a styled frame
    st.markdown('<div class="dashboard-frame">', unsafe_allow_html=True)
    st.image("C:/Users/HP/Desktop/ECHOhealth/assets/dashboard.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Close the container DIV
st.markdown('</div>', unsafe_allow_html=True)
def get_base64_image(image_path):
    """Convert image to base64 for embedding in HTML."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Convert QR code image to base64
qr_base64 = get_base64_image("C:/Users/HP/Desktop/ECHOhealth/assets/wqr.png")

# Inject CSS for the section styling
st.markdown("""
    <style>
        /* Main container for the "Get Reports Instantly" section */
        .report-section {
            background-color: #fde4ec;
            padding: 40px;
            border-radius: 16px;
            border: 2px solid #b31bbf; /* Purple border */
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            justify-content: space-between;
            max-width: 900px;
            margin: 30px auto; /* Centers the section horizontally */
        }
        /* Text container styling */
        .report-text {
            flex: 1;
            margin-right: 30px;
        }
        .report-text h2 {
            font-size: 28px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #000;
        }
        .report-text p {
            font-size: 16px;
            color: #555;
            margin: 5px 0;
        }
        .whatsapp-command {
            font-family: 'Courier New', Courier, monospace;
            font-size: 16px;
            font-weight: bold;
            color: #000;
            margin-top: 15px;
        }
        .whatsapp-number {
            font-size: 18px;
            font-weight: bold;
            color: #000;
            margin-top: 5px;
        }
        /* QR code container styling */
        .report-image {
            flex: 0 0 auto;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .report-image img {
            width: 180px; /* Adjust this value if needed */
            height: auto;
        }
    </style>
""", unsafe_allow_html=True)

# Build the section layout
st.markdown(f"""
<div class="report-section">
    <div class="report-text">
        <h2>Get Reports Instantly</h2>
        <p>Generate comprehensive reports and act immediately on your voice health.</p>
        <p class="whatsapp-command">➤ Send <b>join put-rice</b> to</p>
        <p class="whatsapp-number"><b>WhatsApp</b> +1 415 523 8886</p>
    </div>
    <div class="report-image">
        <img src="data:image/png;base64,{qr_base64}" alt="QR Code">
    </div>
</div>
""", unsafe_allow_html=True)

def get_base64_image(image_path):
    """Convert an image file to a base64 string."""
    with open(image_path, "rb") as file:
        data = file.read()
    return base64.b64encode(data).decode()

# -- Hide Streamlit UI + Remove Extra Page Padding --

st.markdown("""
    <style>
    /* Hide default Streamlit menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Remove extra padding/margin from the main container */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }
    </style>
""", unsafe_allow_html=True)

# -- CSS Styling --
st.markdown("""
    <style>
        /* Container for the feature cards */
        .final-landing-container {
            background-image: linear-gradient(white, white), url('https://www.transparenttextures.com/patterns/cubes.png');
            background-size: cover;
            padding: 50px 0;
            /* Removed bottom margin to eliminate extra space */
            margin: 0 auto;
            max-width: 1100px;
        }

        /* Features row styling */
        .features-container {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            margin-bottom: 50px;
        }
        .feature-card {
            background-color: #fff;
            width: 30%;
            min-width: 250px;
            margin: 10px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            padding: 20px;
            text-align: center;
        }
        .feature-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #000;
        }
        .feature-description {
            font-size: 14px;
            color: #555;
            line-height: 1.4em;
        }

        /* Full-width Feedback Section */
        .feedback-section {
            background-color: #e91e63;
            text-align: center;
            padding: 40px 20px;
            margin: 0;
            border-radius: 0;
            width: 100vw;  /* Force full browser width */
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw; /* Shift to full width */
            margin-right: -50vw;
        }
        .feedback-section h2 {
            font-size: 26px;
            font-weight: bold;
            color: #fff;
            margin-bottom: 10px;
        }
        .feedback-section p {
            font-size: 16px;
            color: #fce4ec;
            margin-bottom: 20px;
        }
        .feedback-button {
            background-color: #fff;
            color: #e91e63;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        .feedback-button:hover {
            background-color: #f8bbd0;
        }
    </style>
""", unsafe_allow_html=True)

# --- HTML Content (Features + Feedback) ---
st.markdown("""
    <!-- Features Section -->
    <div class="final-landing-container">
        <div class="features-container">
            <div class="feature-card">
                <h3 class="feature-title">Voice Analysis</h3>
                <p class="feature-description">
                    Advanced AI algorithms analyze your voice patterns to detect potential issues and track improvements.
                </p>
            </div>
            <div class="feature-card">
                <h3 class="feature-title">Personalized Exercises</h3>
                <p class="feature-description">
                    Get tailored vocal exercises based on your voice analysis results and goals.
                </p>
            </div>
            <div class="feature-card">
                <h3 class="feature-title">Progress Tracking</h3>
                <p class="feature-description">
                    Monitor your vocal health improvements over time with detailed progress reports.
                </p>
            </div>
        </div>
    </div>

    <!-- Full-Width Feedback Section -->
    <div class="feedback-section">
        <h2>Share Your Voice Journey</h2>
        <p>Help us improve by sharing your experience with EchoHealth</p>
        <button class="feedback-button">Give Feedback</button>
    </div>
""", unsafe_allow_html=True)
# Custom CSS for Sidebar
st.markdown("""
    <style>
        /* Sidebar Container */
        [data-testid="stSidebar"] {
            background-color: #ffffff !important; /* White Background */
            border-right: 2px solid #f0f0f5 !important; /* Light Gray Border */
            padding-top: 20px;
        }

        /* Sidebar Title */
        [data-testid="stSidebarNav"] h2 {
            color: #ff007f !important; /* Pinkish Theme */
            font-size: 24px !important;
            font-weight: bold !important;
            text-align: center;
        }

        /* Sidebar Links */
        [data-testid="stSidebarNav"] a {
            color: #333333 !important; /* Dark Gray */
            font-size: 16px !important;
            font-weight: 600 !important;
            padding: 12px 20px !important;
            display: block;
            border-radius: 8px;
            transition: all 0.3s ease-in-out;
        }

        /* Hover Effect */
        [data-testid="stSidebarNav"] a:hover {
            background-color: #ff007f !important; /* Pink Hover */
            color: white !important;
        }

        /* Active Tab */
        [data-testid="stSidebarNav"] .css-1e5imcs {
            background-color: #ff007f !important;
            color: white !important;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

