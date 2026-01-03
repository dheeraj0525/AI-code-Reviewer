# AI-code-Reviewer
---
🧠 AI Code Reviewer & Debugging Tool
An AI-powered web application that analyzes C++ and Python code, detects errors, explains mistakes in simple language, and suggests corrected versions — built to help developers debug faster and learn better.

---
🚀 Why This Project Exists
Beginner and intermediate programmers often struggle with:
Understanding compiler/runtime errors
Debugging logical mistakes
Learning why code fails, not just fixing it
This tool bridges that gap by combining software engineering principles with LLM-powered code analysis, delivering clear explanations instead of cryptic error messages.

---
✨ Features
🔍 Analyze C++ and Python source code
🧠 Detect syntax and logical errors
📘 Human-readable explanations of mistakes
✅ AI-generated corrected code suggestions
⚡ Fast backend built with FastAPI
🌐 Simple web-based interface

---
🛠️ Tech Stack
Backend
Python
FastAPI
OpenAI API
Pydantic
Uvicorn
Frontend
HTML
CSS
JavaScript
Tools
Git & GitHub
Virtual Environment (venv)

---

🏗️ Project Architecture

ai-code-reviewer/
│
├── backend/
│   ├── main.py          # FastAPI entry point
│   ├── prompts.py       # Prompt engineering logic
│   ├── schemas.py       # Request/response models
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── .env
└── README.md

---
⚙️ How It Works
1. User submits source code and selects a language
2. Backend sends structured prompt to the LLM
3. AI analyzes the code and returns:
Errors
Explanation
Corrected version
4. Results are displayed in real time on the frontend

---
🧪 Example Use Case
Input (C++):

int main() {
  cout << "Hello World"
}
Output:
Missing semicolon
Missing #include <iostream>
Corrected code with explanation

---

▶️ Getting Started (Local Setup)

1. Clone the repository
git clone https://github.com/dheeraj0525/ai-code-reviewer.git
cd ai-code-reviewer

2. Create & activate virtual environment
Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Add environment variables
Create a .env file in the root directory:
OPENAI_API_KEY=your_api_key_here

---

5. Run the backend
uvicorn backend.main:app --reload
Open in browser:
http://127.0.0.1:8000/docs

---

📌 Future Enhancements

Support for more programming languages
User authentication & history
Advanced static analysis
Code quality scoring
Deployment (Docker / Cloud)

---

👤 Author

Dheeraj Aryan
BCA (AI & Data Science)
Aspiring Software / AI Engineer
