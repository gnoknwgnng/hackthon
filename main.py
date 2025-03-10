import streamlit as st
import requests

# Set up the Streamlit app
st.title("AI-Powered Solutions Hub")

# List of AI applications
apps = [
    "Audio Transcription App using OpenAI Whisper",
    "SmartResume Generator: Customized Resumes for Every Opportunity",
    "Empowering Career Progression with Tailored Cover Letters",
    "TransLingua: AI-Powered Multi-Language Translator",
    "CareWise: AI Symptom Checker and Treatment Advisor",
    "VisionTagger AI: Advanced Image Tagging with Gemini Vision Pro",
    "AI Personalized Email Generator",
    "StudBud: AI Study Planner",
    "WriteWise: Essay and Assignment Feedback Tool",
    "Gemini Pro Financial Decoder",
    "LogoCraft: AI Logo Generator with Diffusion Technology",
    "CoutureAI: AI Clothing Image Generator",
    "DataQueryAI: Intelligent Data Analysis with Google TAPAS",
    "JobSwift: AI-Powered Job Application Assistant",
    "Project Insight: AI Feedback for Development Teams",
    "DocuQuery: AI-Powered PDF Knowledge Assistant"
]

# Select an AI application
selected_app = st.selectbox("Choose an AI solution to use:", apps)

# Hardcoded Gemini API Key (not recommended for security reasons)
GEMINI_API_KEY = "AIzaSyBy2vvh02Jrc0dzdeKtxQTr8JdlVeZ5EfE"  # Replace with your actual key

# Dictionary mapping apps to Gemini models (fixed)
app_to_model = {
    "SmartResume Generator: Customized Resumes for Every Opportunity": "gemini-pro",
    "Empowering Career Progression with Tailored Cover Letters": "gemini-pro",
    "WriteWise: Essay and Assignment Feedback Tool": "gemini-pro",
    "Gemini Pro Financial Decoder": "gemini-pro",
    "CareWise: AI Symptom Checker and Treatment Advisor": "gemini-pro",
    "VisionTagger AI: Advanced Image Tagging with Gemini Vision Pro": "gemini-pro-vision",
    "AI Personalized Email Generator": "gemini-pro",
    "StudBud: AI Study Planner": "gemini-pro",
    "TransLingua: AI-Powered Multi-Language Translator": "gemini-pro",
    "DataQueryAI: Intelligent Data Analysis with Google TAPAS": "gemini-pro",
    "JobSwift: AI-Powered Job Application Assistant": "gemini-pro",
    "Project Insight: AI Feedback for Development Teams": "gemini-pro",
    "DocuQuery: AI-Powered PDF Knowledge Assistant": "gemini-pro"
}

# Define function to call Gemini API
def call_gemini_api(model, input_text):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateText?key={GEMINI_API_KEY}"
    payload = {"prompt": {"text": input_text}}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise error for 4xx/5xx responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# User input for the selected AI application
user_input = st.text_area("Enter your input text (if applicable):")

# Run AI model when button is clicked
if st.button("Generate Output"):
    if user_input:
        model = app_to_model.get(selected_app, "gemini-pro")  # Default to "gemini-pro" if not found
        result = call_gemini_api(model, user_input)

        st.write("### Output:")
        st.write(result)
    else:
        st.error("Please enter input text.")
