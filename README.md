# Gemini AI Chatbot (LangGraph + FastAPI + Streamlit)

An interactive AI-powered chatbot built with **FastAPI** as the backend, **Streamlit** as the frontend, and **LangGraph** to manage conversation flows. It uses the **Gemini API** for advanced language generation, allowing the bot to understand and respond intelligently to user queries.

---

## ✨ Features

- 💬 Conversational AI powered by **Gemini 2.0 Flash Lite**  
- ⚡ FastAPI backend that maintains **chat history** (`chat_history.json`)  
- 💻 Streamlit frontend for a smooth, interactive experience  
- 📥 Option to **download chat history**  
- ☁️ Fully runs in **Google Colab** with public ngrok links  
- 🧠 **LangGraph** manages multi-turn conversation flows  

---

## 📦 Installation

Run this in a Colab notebook cell to install dependencies:

```bash
!pip install -qU langchain_google_genai langgraph fastapi uvicorn nest-asyncio pyngrok streamlit requests
🚀 Usage

Run the FastAPI backend:
Start the backend server to handle chatbot requests.

Launch Streamlit frontend:
Open the frontend interface to interact with the chatbot.

Start chatting:
Type your messages, and the AI responds in real-time.

💡 Creative Use-Cases

Recipe Assistant – Suggests recipes based on available ingredients.

Educational Tutor – Explains concepts and solves problems.

Personal Finance Advisor – Offers budgeting tips and financial guidance.

Mental Health Companion – Provides supportive conversation or mood tracking.

🛠 Tech Stack

Frontend: Streamlit

Backend: FastAPI

Conversation Management: LangGraph

AI Model: Google Generative AI (Gemini)

📄 License

This project is licensed under the MIT License.

🔗 Acknowledgements

FastAPI

Streamlit

LangGraph

Google Generative AI (Gemini)
