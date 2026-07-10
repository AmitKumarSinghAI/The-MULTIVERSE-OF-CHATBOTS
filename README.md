# 🌌 The Multiverse of Chatbots

### MirAI School of Technology - Virtual Summer Internship 2026  
### AI Builder Track - Assignment 2

This is my second assignment completed during the Virtual Summer Internship 2026 at **MirAI School of Technology** under the **"AI Builder" Track**.

The project is called **"The Multiverse of Chatbots"**. It is an interactive AI chatbot web application developed using **Streamlit** and **Google Gemini API** that allows users to communicate with different AI personalities. The application uses prompt engineering techniques to make the AI respond while staying in a selected character/personality.

---

# 🚀 Project Overview

The Multiverse of Chatbots is a Generative AI application where users can select different personalities and interact with an AI chatbot.

The application sends user instructions to the Gemini Large Language Model (LLM) and generates creative, personality-based responses.

Users can talk with different AI personas such as:

- 🧑‍💻 Expert Hacker
- 🏏 Angry Ravi Shastri
- ⚽ Crazy Ronaldo Fan
- 🎯 Motivational Coach
- 💻 Sarcastic Programmer

The project demonstrates the practical use of:

- Large Language Models (LLMs)
- Prompt Engineering
- API Integration
- Streamlit Web Development
- Environment Variable Management

---

# ✨ Features

✅ Interactive Streamlit user interface  
✅ Multiple AI personalities  
✅ Google Gemini 2.5 Flash model integration  
✅ Dynamic prompt generation  
✅ Secure API key handling using environment variables  
✅ User input validation  
✅ Loading indicator during AI response generation  
✅ Error handling for API failures  

---

# 🛠️ Technologies Used

### Programming Language
- Python

### AI / LLM
- Google Gemini API
- Gemini 2.5 Flash Model
- Prompt Engineering

### Framework
- Streamlit

### Libraries

- streamlit
- google-genai
- python-dotenv

---

# 📂 Project Structure

```
Multiverse-Chatbots/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .gitignore             # Ignored files
│
└── .env                   # API keys (Not uploaded)
```

---

# ⚙️ Installation and Setup

## 1. Clone the repository

```bash
git clone https://github.com/AmitKumarSinghAI/The-MULTIVERSE-OF-CHATBOTS
```

## 2. Navigate into the project folder

```bash
cd Multiverse-Chatbots
```

## 3. Create virtual environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Setup Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

---

# ▶️ Run the Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

# 🧠 How It Works

1. User selects an AI personality.
2. User enters a message.
3. The application creates a custom prompt using the selected personality.
4. The prompt is sent to the Gemini API.
5. Gemini generates a response according to the selected character.
6. The response is displayed in the Streamlit interface.

---

# 🔐 API Key Security

The Gemini API key is stored securely using environment variables.

The `.env` file is excluded from GitHub using `.gitignore`.

Example:

```
.env
```

Never upload API keys or private credentials to public repositories.

---

# 📸 Application Preview

(Add screenshots of your Streamlit application here)

---

# 🎯 Learning Outcomes

Through this assignment, I learned:

- How to integrate LLM APIs into applications
- How to build AI-powered web interfaces using Streamlit
- How prompt engineering controls AI behavior
- How to handle API errors
- How to manage sensitive information securely

---

# 👨‍💻 Author

**Amit Kumar Singh Kurmi**

AI Builder Track  
Virtual Summer Internship 2026  
MirAI School of Technology