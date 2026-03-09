# 🤖 AI Code Review & Debugging Tool

AI Code Review & Debugging Tool is a web-based application that analyzes source code and provides automated feedback such as potential errors, explanations, and improved versions of the code.

The goal of this project is to demonstrate how **AI-powered developer tools** can be built using a modern backend framework and exposed through clean REST APIs, similar to tools used in real-world software engineering workflows.

This project focuses more on **backend engineering, API design, and system integration** rather than UI complexity.

---

## 🚀 Features

* Paste source code and select programming language
* AI-based code review and debugging feedback
* Error detection and explanation
* Suggested corrected code
* REST API built with FastAPI
* Auto-generated API documentation (Swagger)
* Demo mode support (works without OpenAI API credits)

---

## 🧠 How It Works

1. User pastes code and selects the language in the frontend UI
2. Frontend sends a POST request to the FastAPI backend
3. Backend prepares a structured prompt for AI analysis
4. AI analyzes the code and returns:

   * Errors
   * Explanation
   * Corrected code
5. The response is displayed in the UI in a readable format

When no OpenAI API key is configured, the system automatically runs in **demo mode** to simulate AI responses.

---

## 🛠 Tech Stack

### Backend

* Python
* FastAPI
* OpenAI API
* Pydantic (data validation)
* REST APIs

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Tools & Concepts

* API-based architecture
* Environment variables
* Error handling
* JSON-based communication

---

## 📁 Project Structure

```
ai-code-reviewer/
│
├── backend/
│   ├── main.py
│   ├── schemas.py
│   ├── prompts.py
│   └── __init__.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── screenshots/
│   ├── ui-input.png
│   ├── output-result.png
│   ├── api-docs.png
│   └── analyze-endpoint.png
│
├── requirements.txt
└── README.md
```

---

## 📷 Screenshots

### Code Input Interface

![Input Interface](screenshots/ui-input.png)

### AI Analysis Output

![Analysis Output](screenshots/output-result.png)

### API Documentation (Swagger)

![API Docs](screenshots/api-docs.png)

### Analyze Endpoint

![Analyze Endpoint](screenshots/analyze-endpoint.png)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dheeraj0525/AI-code-Reviewer.git
cd AI-code-Reviewer
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Environment Variables (Optional)

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ If the API key is not provided, the application runs in **demo mode**.

---

## ▶️ Run the Application

### Start Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

### Start Frontend

```bash
cd frontend
python -m http.server 5500
```

Frontend runs at:

```
http://localhost:5500
```

---

## 📄 API Documentation

FastAPI provides automatic API documentation:

* Swagger UI

  ```
  http://127.0.0.1:8000/docs
  ```

* ReDoc

  ```
  http://127.0.0.1:8000/redoc
  ```

---

## 🧪 Example API Request

**POST** `/analyze`

```json
{
  "code": "int main(){ cout << \"Hello\"; }",
  "language": "C++"
}
```

**Response**

```json
{
  "errors": ["Missing include for iostream"],
  "explanation": "The cout object requires the iostream header.",
  "corrected_code": "#include <iostream>\nint main(){ std::cout << \"Hello\"; }"
}
```

---

## 🚧 Limitations

* Output quality depends on AI model
* Currently supports basic code review scenarios
* Not a replacement for human code review

---

## 🔮 Future Improvements

* GitHub repository integration
* Support for more programming languages
* Static code analysis (rule-based checks)
* Authentication & user history
* Deployment as a hosted SaaS tool

---

## 👨‍💻 Author

**Dheeraj Aryan**
BCA Student | Aspiring Software Engineer
GitHub: [https://github.com/dheeraj0525](https://github.com/dheeraj0525)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Why This Project Matters

This project demonstrates:

* API-driven backend development
* AI integration in real applications
* Clean request/response design
* Practical handling of real-world constraints (demo mode)

It reflects how modern developer tools are built and deployed in industry environments.
