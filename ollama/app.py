# Importing dependencies
import streamlit as st
from langchain_community.llms import Ollama
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

def generate_response(question, engine, temperature):
    try:
        llm = Ollama(
            model=engine,
            temperature=temperature,
            #max_output_tokens=max_tokens, # Old Ollama models do not have max output tokens feature. Newer versions use `num_predict` instead
        )

        chain = prompt | llm

        return chain.stream({"question": question})

         

    except Exception as e:
        return f"Error:\n{e}"


# Title of the app
st.title("Q&A Chatbot With Ollama")

# Select the LLM model
engine = st.sidebar.selectbox(
    "Select Ollama model",
    [
        "llama3:latest",
        "gemma:2b",
    ]
)

# Adjust response parameter
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)

# Main interface for user input
st.write("Ask away!")
user_input=st.text_input("You:")

# Loop for 
if user_input:
    response=generate_response(user_input,engine,temperature)
    placeholder = st.empty()
    full_response = ""

    for chunk in response:
        full_response += chunk
        placeholder.markdown(full_response)
else:
    st.warning("_Please provide the user input._")