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

# Gemini API key (Integrated into the code)
gemini_api_key = "AIzaSyBy2vvh02Jrc0dzdeKtxQTr8JdlVeZ5EfE"

def call_gemini_api(model, input_text):
    url = f"https://api.gemini.com/v1/{model}/generate"
    headers = {"Authorization": f"Bearer {gemini_api_key}"}
    payload = {"inputs": input_text}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

# Process user input based on selected app
user_input = st.text_area("Enter your input text (if applicable):")
if st.button("Generate Output"):
    if user_input:
        if selected_app == "Audio Transcription App using OpenAI Whisper":
            model = "openai/whisper"
        elif selected_app == "SmartResume Generator: Customized Resumes for Every Opportunity":
            model = "gemini/resume-generator"
        elif selected_app == "Empowering Career Progression with Tailored Cover Letters":
            model = "gemini/cover-letter"
        elif selected_app == "TransLingua: AI-Powered Multi-Language Translator":
            model = "gemini/translator"
        elif selected_app == "CareWise: AI Symptom Checker and Treatment Advisor using Palm's chat-bison-001":
            model = "gemini/health-checker"
        elif selected_app == "VisionTagger AI: Leveraging Google's Gemini Vision Pro for Advanced Image Tagging and Detailed JSON Metadata":
            model = "gemini/vision-pro"
        elif selected_app == "AI Personalized Email Generator":
            model = "gemini/email-generator"
        elif selected_app == "StudBud: AI Study Planner":
            model = "gemini/study-planner"
        elif selected_app == "WriteWise: Essay and Assignment Feedback Tool using Bert and T5":
            model = "gemini/essay-feedback"
        elif selected_app == "Gemini Pro Financial Decoder":
            model = "gemini/financial-decoder"
        elif selected_app == "LogoCraft: Innovative Logo Generation with Diffusion Technology":
            model = "gemini/logo-generator"
        elif selected_app == "CoutureAI: Clothing Image Generator Using Stable Diffusion Pipeline":
            model = "gemini/clothing-generator"
        elif selected_app == "DataQueryAI: Intelligent Data Analysis with Google TAPAS":
            model = "gemini/data-analysis"
        elif selected_app == "JobSwift: Accelerating Careers with AI-Powered Applications using Palm's text-bison-001":
            model = "gemini/job-application"
        elif selected_app == "Project Insight: AI Feedback Generator for Development Teams using Palm's models/text-bison-001":
            model = "gemini/project-feedback"
        elif selected_app == "DocuQuery: AI-Powered PDF Knowledge Assistant Using Google PALM":
            model = "gemini/pdf-assistant"
        else:
            model = "gemini/default-model"

        result = call_gemini_api(model, user_input)
        st.write("### Output:")
        st.write(result)
    else:
        st.error("Please enter input text.")
