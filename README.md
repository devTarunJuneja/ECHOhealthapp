EchoHealth: AI-Powered Voice Pathology Detection

EchoHealth is an AI-driven platform designed to detect laryngeal voice disorders using machine learning. It empowers users to assess vocal health and provides personalized recommendations for better care.

Features

🎙️ Voice Pathology Detection: Predicts laryngeal disorders from audio features.

🤖 Health Assistant Chatbot: Offers health advice using Google Gemini API.

📊 User Dashboard: Tracks reports and progress.

🏋️ Exercise Panel: Suggests vocal exercises.

🔐 Authentication: Integrated Supabase for secure login.

Tech Stack

Frontend: Streamlit

Backend: Python (with scikit-learn, joblib, numpy, pandas)

Authentication: Supabase

AI Chatbot: Google Gemini API

Project Structure

EchoHealth/
├── backend/                 # Backend logic & ML model
│   ├── main.py             # Backend API & ML processing
│   ├── model.py            # Model loading & predictions
│   ├── preprocess.py       # Data preprocessing functions
│   └── utils.py            # Helper functions
├── frontend/                # Streamlit-based frontend
│   ├── app.py              # Streamlit app
│   ├── components/         # Custom UI components
│   ├── pages/              # Multi-page structure
│   └── styles/             # CSS for UI styling
├── models/                 # ML model
│   └── laryngeal-voice-disorder-classification.pkl
├── requirements.txt         # Project dependencies
├── .env                     # Environment variables
└── README.md                # Documentation

Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/echohealth.git
cd echohealth

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up environment variables:
Create a .env file in the root directory:

SUPABASE_URL=<your-supabase-url>
SUPABASE_KEY=<your-supabase-key>
GEMINI_API_KEY=<your-gemini-api-key>

Run the app:

streamlit run frontend/app.py

Usage

Upload your voice sample.

Click "Analyze" to get predictions.

Access personalized reports and health insights.

Chat with the Health Assistant for vocal health tips.

Contributing

Contributions are welcome! Feel free to fork the repo and submit pull requests.

License

MIT License

Contact

For inquiries, reach out to Tarun Juneja at [your email].

Empower vocal health with AI — EchoHealth 🚀

"# ECHOhealthapp" 
