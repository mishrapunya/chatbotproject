import streamlit as st

st.title("My Chatbot")
st.write("Hello! How can I help you today?")

user_input = st.text_input("Ask me something:")
if user_input:
    st.write(f"You said: {user_input}")
