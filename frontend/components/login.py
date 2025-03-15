import streamlit as st

# Set page configuration
st.set_page_config(page_title="Login - EchoHealth", layout="centered")

# Custom CSS for the login page (soft gradient, light pink accents)
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #ffffff, #ffeef3);
    font-family: 'Arial', sans-serif;
}
.login-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 40px;
    background-color: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.login-header {
    text-align: center;
    margin-bottom: 30px;
}
.login-header h2 {
    color: #e75480;
    margin-bottom: 5px;
}
.login-header p {
    color: #666;
    font-size: 14px;
}
.stTextInput>div>div>input {
    border: 1px solid #ffeef3;
    border-radius: 5px;
}
.stButton>button {
    background-color: #e75480;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
}
.stButton>button:hover {
    background-color: #d74370;
}
.additional-links {
    text-align: center;
    margin-top: 20px;
}
.additional-links a {
    color: #e75480;
    text-decoration: none;
    font-size: 14px;
}
.additional-links a:hover {
    text-decoration: underline;
}
.footer {
    text-align: center;
    margin-top: 30px;
    font-size: 12px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# Login page container
st.markdown("<div class='login-container'>", unsafe_allow_html=True)

# Header with logo text and tagline
st.markdown("""
<div class='login-header'>
    <h2>EchoHealth Login</h2>
    <p>Access your personalized voice health dashboard</p>
</div>
""", unsafe_allow_html=True)

# Create the login form
with st.form("login_form", clear_on_submit=True):
    email = st.text_input("Email", placeholder="Enter your email")
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    login_button = st.form_submit_button("Login")

# Check login credentials
if login_button:
    if username == "Tarunjuneja" and password == "123":
        st.success(f"Welcome, {username}! Redirecting to Home Page...")
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.experimental_set_query_params(page="app")  # Redirect to home
        st.experimental_rerun()
    else:
        st.error("Invalid username or password")

# Additional links (Forgot password? / Sign Up)
st.markdown("""
<div class='additional-links'>
    <a href="#">Forgot password?</a> | <a href="#">Sign Up</a>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    Powered by EchoHealth
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
