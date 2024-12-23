# Libraries Importation
import streamlit as st
import openai
import time
import os
import sys
import openai
from dotenv import load_dotenv

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from utils import predLung_Disease, set_background
set_background('./bckgrd_image/mental_bckgrd.jpg')

load_dotenv()

# Initialize the OpenAI API client
openai.api_key = os.getenv("sk-jt6dzKKXFAF7COcW5TM9Kr7dCKUH6AcwLSbGizqryJT3BlbkFJ-HOV2hRQBU5DfoeP-7yYXVoZPFFzxMnvce72w5AE4A")

system_prompt = "You are a mental health support bot who helps users understand their mental health situation and get answers to their questions."

def mentalChatBot(userInput):
    system_prompt = '''You are a mental health support bot assistant who helps users understand their 
                    mental health situation and get answers to their questions.
                    Identify early warning signs of mental health struggles and encourage users 
                    to seek professional support when needed.
                    First analyze the user question and do not provide response if the question is not related to mental health such as
                    user asking about travel advice, entertainment, etc.'''


    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": userInput}
        ]
    )
    chatbot_response = response.choices[0].message.content
    return chatbot_response

st.title("AI MedCheck: Mental Health Chatbot")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What can I do for you?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in mentalChatBot(prompt):
            full_response += response
            message_placeholder.markdown(full_response)
            time.sleep(0.05)
    print(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
