[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://simple-qna-chatbot-nzkfy8u74npcylxa5fgqy9.streamlit.app/)
# Q&A Chatbot with LangChain

A simple Q&A chatbot built while learning **LangChain** and **Streamlit**. The project includes two implementations:

- **Google Gemini** using the Google Gen AI API
- **Ollama** for running local LLMs

Both versions demonstrate prompt engineering, model configuration, LangChain chains, response streaming, and integration with different LLM providers.

## 🚀 Live Demo

Try the chatbot here:

**🌐** https://simple-qna-chatbot-nzkfy8u74npcylxa5fgqy9.streamlit.app/
> **Note:** You'll need your own **Google Gemini API Key** to use the Google Gen AI version of the chatbot. You can get one for free from Google AI Studio.

---

## Features

- Interactive Streamlit web interface
- Supports multiple LLM providers
  - Google Gemini
  - Ollama (local models)
- Custom system prompts using `ChatPromptTemplate`
- Real-time response streaming
- Adjustable model parameters
  - Temperature
  - Maximum output tokens
- LangSmith tracing support for debugging (optional)

## Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API
- Ollama
- LangSmith
- python-dotenv

## What I Learned

- Building AI applications with LangChain
- Creating reusable prompts using `ChatPromptTemplate`
- Understanding LangChain chains (`prompt | llm | parser`)
- The difference between `invoke()` and `stream()`
- Using `StrOutputParser`
- Streaming responses in Streamlit
- Integrating cloud models (Google Gemini)
- Running local models with Ollama
- Using LangSmith to trace and debug LLM applications
- Managing API keys securely using `.env`
- Configuring model parameters such as temperature and output tokens

## Project Structure

```
QNA Chatbot/
│
├── google_gen_ai/
│   └── app.py                 # Google Gemini chatbot
│
├── ollama/
│   └── app.py                # Ollama chatbot
│
├── requirements.txt
├── pyproject.toml
├── .env                       # Environment variables (not committed)
├── .gitignore
└── README.md
```

## Installation

```bash
git clone <your-repository-url>

cd <repository>

pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
LANGCHAIN_API_KEY=your_langsmith_key   # Optional
```

## Run the Application

```bash
streamlit run app.py
```

## Future Improvements

- Chat history
- Conversation memory
- File upload support
- RAG using PDFs
- Multiple prompt templates
- Dark/light themes
- Deployment on Streamlit Community Cloud

---

Built while learning LangChain and modern LLM application development.