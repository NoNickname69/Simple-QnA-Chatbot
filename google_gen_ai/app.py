# Importing dependencies
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
# Loading API key
from dotenv import load_dotenv
load_dotenv()
# Optional LangSmith
langsmith_key = os.getenv("LANGCHAIN_API_KEY")

if langsmith_key:
    os.environ["LANGCHAIN_API_KEY"] = langsmith_key
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A Chatbot With Google Gen AI"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",
            """You are an intelligent, reliable, and friendly AI assistant.

            Guidelines:
            - Answer accurately and honestly.
            - If information is uncertain, clearly state the uncertainty.
            - Be concise by default, but provide detailed explanations when requested.
            - Organize responses with headings, bullet points, and Markdown when helpful.
            - Explain technical concepts clearly and include examples when beneficial.
            - Never fabricate facts, sources, or code.
            - Maintain a professional, respectful, and conversational tone."""),
        ("user","Question:{question}")
    ]
)

# Defining a response generator using Google Gen AI models

def generate_response(question, api_key, engine, temperature, max_tokens):
    try:
        llm = ChatGoogleGenerativeAI(
            model=engine,
            google_api_key=api_key,
            temperature=temperature,
            max_output_tokens=max_tokens,
        )

        chain = prompt | llm

        return chain.stream({"question": question})

         

    except Exception as e:
        return f"Error:\n{e}"


# Title of the app
st.title("Q&A Chatbot With Google Gen AI")

# Sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter your Google Gen AI API Key:",
                              type="password",
                              help="""
                                **How to get your API key:**

                                1. Visit https://aistudio.google.com/app/apikey
                                2. Sign in with your Google account.
                                3. Click **Create API Key**.
                                4. Copy the generated key.
                                5. Paste it here.

                                Your API key is only used for requests from this app and is not stored.
                                """)

# Select the LLM model
engine = st.sidebar.selectbox(
    "Select Gemini model",
    [
        "gemini-2.5-flash",
        "gemini-2.5-pro",
    ]
)

# Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=24, max_value=2048, value=1024)

# Main interface for user input
st.write("Ask away!")
user_input=st.text_input("You:")

# Loop for 
if user_input and api_key:
    response=generate_response(user_input,api_key,engine,temperature,max_tokens)
    placeholder = st.empty()
    full_response = ""

    for chunk in response:
        full_response += chunk.content
        placeholder.markdown(full_response)
elif user_input:
    st.warning("_Please enter the AI API Key in the sidebar._")
else:
    st.warning("_Please provide the user input._")