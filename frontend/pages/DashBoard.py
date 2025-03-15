import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Voice Health Dashboard", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Overall page background */
    .css-18e3th9 {
        background-color: #f7f7f7 !important;
    }

    /* Title & subtitle */
    .header-title {
        margin-bottom: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 2rem;
    }
    .header-subtitle {
        color: gray;
        margin-top: 0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 1rem;
    }

    /* Container for main sections (outer boundary) */
    .custom-box {
        background: #ffffff;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-top: 0px !important;    /* No extra gap above */
        margin-bottom: 20px !important;
    }

    /* Start New button */
    .stButton>button {
        background-color: #ff4081;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
    }

    /* Reduce top padding for main container */
    .css-1y4p8pa {
        padding-top: 1rem !important;
    }

    /* Remove extra space BELOW the tab bar */
    .stTabs [data-baseweb='tab-list'] {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
        border-bottom: none !important;
    }

    /* Remove extra space ABOVE the tab bar (if any) */
    .stTabs [data-baseweb='tab-list'] > div {
        margin-top: 0px !important;
        padding-top: 0px !important;
    }

    /* Remove margins on each tab (optional) */
    .stTabs [role='tab'] {
        margin: 0px !important;
        padding: 0.5rem 1rem !important; /* Adjust padding as desired */
    }

    /* Optionally remove the border around the active tab (uncomment if needed)
    .stTabs [aria-selected='true'] {
        border-bottom: none !important;
    }
    */

    /* (Optional) If there's still a gap, you can use negative margin:
       .custom-box {
           margin-top: -10px !important;
       }
    */
    </style>
    """,
    unsafe_allow_html=True,
)

# ----- HEADER (Title, Subtitle, Button) -----
st.markdown("<h1 class='header-title'>Voice Health Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h4 class='header-subtitle'>Track your vocal performance and health</h4>", unsafe_allow_html=True)

# Start New button -> Redirect to diagnosis.py
if st.button("Start New"):
    # JavaScript snippet to redirect
    st.markdown(
        """
        <script>
            window.open('pages/diagnosis.py', '_self');
        </script>
        """,
        unsafe_allow_html=True
    )

# Welcome message
st.markdown("### Welcome Tarun")

# ----- TABS -----
tab_overview, tab_analysis, tab_exercises = st.tabs(["Overview", "Detailed Analysis", "Recommended Exercises"])

# ---------------------- OVERVIEW TAB ----------------------
with tab_overview:
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)

    # Row of metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🎵 Average Pitch", "225 Hz", "+2.5%")
    with col2:
        st.metric("🔊 Volume Level", "72 dB", "+5.0%")
    with col3:
        st.metric("✨ Voice Clarity", "85%", "+3.2%")
    with col4:
        st.markdown("**❤️ Overall Health Score**")
        st.progress(85)  # 85% progress

    # Weekly Progress
    st.markdown("<h3>Weekly Progress</h3>", unsafe_allow_html=True)
    dates = pd.date_range("2024-02-01", periods=6, freq="D")
    values = [78, 79, 80, 79, 81, 80]
    df = pd.DataFrame({"Date": dates, "Health Score": values})

    fig = px.line(df, x="Date", y="Health Score", markers=True, line_shape="linear")
    fig.update_traces(line_color="#ff4081", fill="tozeroy", fillcolor="rgba(255,64,129,0.2)")
    fig.update_layout(
        xaxis_title="",
        yaxis_title="",
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- DETAILED ANALYSIS TAB ----------------------
with tab_analysis:
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.markdown("<h3>Detailed Analysis</h3>", unsafe_allow_html=True)
    st.write("Below is a deeper dive into your voice metrics over the last week.")

    # Sample data for demonstration
    dates = pd.date_range("2024-02-01", periods=7, freq="D")
    pitch =   [220, 225, 222, 226, 224, 230, 228]
    volume =  [70,  72,  71,  73,  74,  72,  75]
    clarity = [82,  84,  83,  85,  86,  88,  87]

    # Create a DataFrame
    df_analysis = pd.DataFrame({
        "Date": dates,
        "Pitch (Hz)": pitch,
        "Volume (dB)": volume,
        "Clarity (%)": clarity
    })

    # Display the raw data in a table
    st.dataframe(
        df_analysis.style.format(
            {
                "Pitch (Hz)": "{:.0f}",
                "Volume (dB)": "{:.0f}",
                "Clarity (%)": "{:.0f}"
            }
        )
    )

    # Create a multi-line chart using Plotly Express
    fig_analysis = px.line(
        df_analysis,
        x="Date",
        y=["Pitch (Hz)", "Volume (dB)", "Clarity (%)"],
        markers=True,
        title="Voice Metrics Over Time"
    )

    fig_analysis.update_layout(
        paper_bgcolor="white",
        plot_bgcolor="white",
        margin=dict(l=20, r=20, t=60, b=20)
    )
    st.plotly_chart(fig_analysis, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- RECOMMENDED EXERCISES TAB ----------------------
with tab_exercises:
    st.markdown("<div class='custom-box'>", unsafe_allow_html=True)
    st.markdown("<h3>Recommended Exercises</h3>", unsafe_allow_html=True)
    
    st.write("Here are some exercises to help maintain and improve your vocal health:")
    
    st.markdown(
        """
        1. **Breathing and Posture**  
           - Stand up straight, shoulders relaxed.  
           - Breathe in through your nose, filling your diaphragm.  
           - Exhale slowly, maintaining a steady stream of air.

        2. **Lip Trills and Humming**  
           - Warm up your vocal cords by gently humming or performing lip trills.  
           - Gradually move up and down in pitch.

        3. **Tongue Twisters**  
           - Practice articulation by repeating short phrases that require clear enunciation.  
           - Examples: "Red leather, yellow leather", "Unique New York".

        4. **Pitch Glides**  
           - Slide from a comfortable low note to a higher note, then back down.  
           - Focus on smooth transitions and consistent tone.
        """
    )

   