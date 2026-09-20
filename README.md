# 🤖 Generative AI Learning & Chatbot

A hands-on Generative AI project where I am learning and experimenting with
LLMs, LangChain, Groq, prompt engineering, conversation memory, and
Streamlit.

This repository contains my initial GenAI experiments and a mood-based
AI chatbot built using LangChain, Groq, and Streamlit.

---

## 🚀 Current Project

### 🤖 Mood Based AI Chatbot

A conversational AI chatbot that allows the user to select different AI
personalities and interact with the LLM through a Streamlit interface.

### Available Modes

- 😡 **Angry Mode** – Responds in an aggressive and impatient tone.
- 😂 **Funny Mode** – Responds with humor and jokes.
- 😢 **Sad Mode** – Responds in a sad and emotional tone.

The chatbot maintains conversation history during the session so that
previous messages can be passed to the LLM for contextual responses.

---

## 🛠️ Tech Stack

- **Python 3.11**
- **LangChain**
- **Groq**
- **GPT-OSS 120B**
- **Streamlit**
- **python-dotenv**
- **uv** – Python package and project management

---

## 🧠 Concepts Practiced

Through this project, I am currently learning and implementing:

- Large Language Models (LLMs)
- LLM APIs
- LangChain
- Chat models
- Prompt engineering
- System prompts
- Human messages
- AI messages
- Conversation history
- Session state
- Temperature
- Streamlit
- Environment variables
- API key management
- Git & GitHub

---

## 📁 Project Structure

```text
GenrativeAI/
│
├── chatbot.py              # Streamlit mood-based chatbot
├── chat.py                 # Basic LangChain + Groq experiment
├── test.py                 # Streamlit testing
├── UIchatbot.py            # UI experimentation
│
├── src/
│   └── genai/
│       └── __init__.py
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── uv.lock
├── requirements.txt
└── README.md
