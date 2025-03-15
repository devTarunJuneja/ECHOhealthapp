import streamlit as st
import requests

# --------------------------------
# 1) PAGE SETUP
# --------------------------------
st.set_page_config(page_title="Voice Health Check", layout="wide")

# --------------------------------
# 2) CUSTOM CSS
# --------------------------------
st.markdown("""
    <style>
    /* Remove default Streamlit padding for a clean look */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Overall background: white */
    .stApp {
        background-color: #ffffff;
        color: #000000;
    }

    /* Pink Heading */
    .diagnosis-title {
        font-size: 36px;
        font-weight: 700;
        color: #FF4DA6;
        text-align: center;
        margin-top: 30px;
        margin-bottom: 8px;
    }

    /* Subtext under heading */
    .diagnosis-subtext {
        font-size: 16px;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Dotted pink box for file upload 
       - Wider, but won't exceed 900px
       - Centered within its container */
    [data-testid="stFileUploadDropzone"] {
        border: 2px dashed #FF4DA6 !important;
        background-color: #FFE6F2 !important; /* light pink */
        border-radius: 10px !important;
        padding: 40px !important;
        text-align: center !important;
        color: #ff4da6 !important;
        margin: 0 auto 30px auto !important;
        width: 100% !important;
        max-width: 900px !important; /* Adjust as needed for max width */
    }

    /* The “Browse files” label in st.file_uploader */
    [data-testid="stFileUploadLabel"] {
        color: #FF4DA6 !important;
        font-weight: 600 !important;
    }

    /* Pink “Start Diagnosis →” button */
    .stButton > button {
        background-color: #FF4DA6 !important;
        color: #ffffff !important;
        border-radius: 30px !important;
        padding: 12px 24px !important;
        border: none !important;
        font-weight: 600 !important;
        cursor: pointer;
        margin: 10px 0 30px 0 !important; /* top 10px, bottom 30px */
    }
    .stButton > button:hover {
        background-color: #ff66b2 !important;
    }

    /* Enhanced Download Button Styling */
    .stDownloadButton button {
        background-color: #FF4DA6 !important;
        color: #ffffff !important;
        border-radius: 30px !important;
        padding: 12px 24px !important;
        border: none !important;
        font-weight: 600 !important;
        cursor: pointer;
        margin-top: 15px !important;
        margin-bottom: 30px !important;
    }
    .stDownloadButton button:hover {
        background-color: #ff66b2 !important;
    }

    </style>
""", unsafe_allow_html=True)

# --------------------------------
# 3) PAGE CONTENT
# --------------------------------

# -- Heading + Subtext
st.markdown("<h1 class='diagnosis-title'>Voice Health Check</h1>", unsafe_allow_html=True)
st.markdown("<p class='diagnosis-subtext'>Upload your audio file in WAV format for diagnosis. Maximum length: 5 seconds.</p>", unsafe_allow_html=True)

col_left, col_mid, col_right = st.columns([0.1, 1.8, 0.1])  # Adjust ratios for spacing
with col_mid:
    uploaded_file = st.file_uploader("", type=["wav", "mp3"])
    # Audio Preview directly below the file uploader
    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/wav")


# -- START DIAGNOSIS BUTTON (Centered)
col_center = st.columns([1.4, 1, 1])[1]
with col_center:
    diagnose_btn = st.button("Start Diagnosis →")

# -- DIAGNOSIS LOGIC
if diagnose_btn and uploaded_file is not None:
    files = {"file": (uploaded_file.name, uploaded_file, "audio/wav")}
    response = requests.post("http://127.0.0.1:8000/predict/", files=files)

    if response.status_code == 200:
        # Save the PDF
        with open("diagnosis_report.pdf", "wb") as f:
            f.write(response.content)

        # ---- Centered "Diagnosis complete" text (no box) ----
        st.markdown("""
            <div style='text-align: center; margin: 20px 0;'>
                <p style='font-size: 18px; color: #FF4DA6; font-weight: 600;'>
                    Diagnosis complete! Download your report below.
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Center the download button
        col_dl_left, col_dl_mid, col_dl_right = st.columns([1.3,1,1])
        with col_dl_mid:
            with open("diagnosis_report.pdf", "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
                st.download_button(
                    label="Download Diagnosis Report",
                    data=pdf_bytes,
                    file_name="diagnosis_report.pdf",
                    mime="application/pdf"
                )
    else:
        st.error("⚠️ Error in processing. Please try again.")
