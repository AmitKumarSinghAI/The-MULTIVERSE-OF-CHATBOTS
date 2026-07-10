from dotenv import load_dotenv
import streamlit as st
from google import genai
import os

load_dotenv()

if "GEMINI_API_KEY" in st.secrets:
    env_var = st.secrets["GEMINI_API_KEY"]
else:
    env_var = os.getenv("GEMINI_API_KEY")

# Check API key
if not env_var:
    st.error("GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

st.set_page_config(
    page_title="Multiverse Chatbot",
    page_icon="🌌"
)


st.title("🌌 The MULTIVERSE OF CHATBOTS")

personality = st.selectbox(
    "Who do you want to talk to?",
    [
        "An expert Hacker",
        "An angry Ravi Shastri",
        "A crazy Ronaldo fan",
        "A motivational coach",
        "A sarcastic programmer"
    ]
)

client = genai.Client(api_key = env_var)

user_message = st.text_input("Say something...")

if st.button("SEND"):
    try:

        if user_message:
            ai_instructions = f"""You are acting as {personality}.
            
            Rules:
             - Stay completely in character.
             - Be creative and engaging.
             - Answer naturally.
             - Do not mention that you are an AI.

             User message:
             {user_message}

            """
            with st.spinner("Connecting to the multiverse!..."):
                response = client.models.generate_content(
                    model = "gemini-2.5-flash",
                    contents = ai_instructions
                )

                st.success("Message received!")
                st.write(response.text)
        else:
            st.error("Please type a message first")

    except Exception as e:
        st.error("Unable to generate response. Please try again later.")
        st.write(e)