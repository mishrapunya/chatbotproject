import streamlit as st
import google.generativeai as genai
import os

# Set up the page
st.title("AI Chatbot with Google Gemini")
st.write("Hello! How can I help you today?")

# Get API Key from environment variable (safer than hardcoding)
import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Google Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Create a function to send queries to Gemini
def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")  # Use the right model
    response = model.generate_content(prompt)
    return response.text  # Extract text response

# User input box
user_input = st.text_input("Ask me anything:")
if user_input:
    response = get_gemini_response(user_input)
    st.write("🤖 Gemini says:", response)
