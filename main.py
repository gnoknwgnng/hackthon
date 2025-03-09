import streamlit as st
import requests

# Set up the Streamlit app
st.title("AI-Powered Solutions Hub")

# List of AI applications
apps = [
    "Gemini Landmark Description App Enhancing Tourist Experiences with AI",
    "Audio Transcription App using OpenAI Whisper",
    "SmartResume Generator: Customized Resumes for Every Opportunity",
    "Empowering Career Progression with Tailored Cover Letters",
    "Playful AI: Intelligent Board Game Opponents and Advisors",
    "FitSync AI: Real-Time Fitness Adjustments with LLaMA3",
    "Flavour Fusion: AI-Driven Recipe Blogging",
    "TransLingua: AI-Powered Multi-Language Translator",
    "CareWise: AI Symptom Checker and Treatment Advisor using Palm's chat-bison-001",
    "VisionTagger AI: Leveraging Google's Gemini Vision Pro for Advanced Image Tagging and Detailed JSON Metadata",
    "AI Personalized Email Generator",
    "StudBud: AI Study Planner",
    "WriteWise: Essay and Assignment Feedback Tool using Bert and T5",
    "Gemini Pro Financial Decoder",
    "LogoCraft: Innovative Logo Generation with Diffusion Technology",
    "CoutureAI: Clothing Image Generator Using Stable Diffusion Pipeline",
    "DataQueryAI: Intelligent Data Analysis with Google TAPAS",
    "JobSwift: Accelerating Careers with AI-Powered Applications using Palm's text-bison-001",
    "Project Insight: AI Feedback Generator for Development Teams using Palm's models/text-bison-001",
    "Shikshak Mahoday: Palm Powered Data Science Tutor",
    "DocuQuery: AI-Powered PDF Knowledge Assistant Using Google PALM"
]

# Select an AI application
selected_app = st.selectbox("Choose an AI solution to use:", apps)

# Placeholder for API key (User needs to input their own API key)
huggingface_api_key = st.text_input("Enter your Hugging Face API Key:", type="password")

# Function to process API calls
def call_huggingface_api(model, input_text):
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {"Authorization": f"Bearer {huggingface_api_key}"}
    payload = {"inputs": input_text}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Process user input based on selected app
user_input = st.text_area("Enter your input text (if applicable):")
if st.button("Generate Output"):
    if huggingface_api_key and user_input:
        if selected_app == "Audio Transcription App using OpenAI Whisper":
            model = "openai/whisper"
        elif selected_app == "SmartResume Generator: Customized Resumes for Every Opportunity":
            model = "bigscience/bloom"
        elif selected_app == "Empowering Career Progression with Tailored Cover Letters":
            model = "bigscience/bloom"
        elif selected_app == "TransLingua: AI-Powered Multi-Language Translator":
            model = "facebook/m2m100_418M"
        elif selected_app == "CareWise: AI Symptom Checker and Treatment Advisor using Palm's chat-bison-001":
            model = "google/palm-chat-bison-001"
        elif selected_app == "VisionTagger AI: Leveraging Google's Gemini Vision Pro for Advanced Image Tagging and Detailed JSON Metadata":
            model = "google/gemini-vision-pro"
        elif selected_app == "AI Personalized Email Generator":
            model = "bigscience/bloom"
        elif selected_app == "StudBud: AI Study Planner":
            model = "bigscience/bloom"
        elif selected_app == "WriteWise: Essay and Assignment Feedback Tool using Bert and T5":
            model = "bert-base-uncased"
        elif selected_app == "Gemini Pro Financial Decoder":
            model = "google/gemini-pro"
        elif selected_app == "LogoCraft: Innovative Logo Generation with Diffusion Technology":
            model = "stabilityai/stable-diffusion-2"
        elif selected_app == "CoutureAI: Clothing Image Generator Using Stable Diffusion Pipeline":
            model = "stabilityai/stable-diffusion-2"
        elif selected_app == "DataQueryAI: Intelligent Data Analysis with Google TAPAS":
            model = "google/tapas-large"
        elif selected_app == "JobSwift: Accelerating Careers with AI-Powered Applications using Palm's text-bison-001":
            model = "google/palm-text-bison-001"
        elif selected_app == "Project Insight: AI Feedback Generator for Development Teams using Palm's models/text-bison-001":
            model = "google/palm-text-bison-001"
        elif selected_app == "DocuQuery: AI-Powered PDF Knowledge Assistant Using Google PALM":
            model = "google/palm-text-bison-001"
        else:
            model = "bigscience/bloom"  # Default model

        result = call_huggingface_api(model, user_input)
        st.write("### Output:")
        st.write(result)
    else:
        st.error("Please enter your Hugging Face API key and input text.")
