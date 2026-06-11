# 🚀 Code Profile Analyzer — AI-Powered Developer Ranking Platform

Code Profile Analyzer is a full-stack AI-powered developer analytics platform that aggregates coding profiles from multiple competitive programming and development platforms.

The platform helps developers analyze coding performance, compare profiles, generate AI-powered career insights, receive personalized skill recommendations, and export professional coding reports.

---

## 🚀 Features

### ✅ Multi-Platform Profile Analysis

Supported Platforms:

* LeetCode
* Codeforces
* GitHub
* GeeksforGeeks
* HackerRank
* CodeChef

Automatically fetches and analyzes coding profiles from multiple platforms.

---

### ✅ Authentication System

Secure user management with:

* User Signup
* User Login
* JWT Authentication
* Protected Routes
* Secure Session Management

---

### ✅ Unified Developer Dashboard

Analyze coding performance using:

* Total Score Calculation
* Profile Strength Meter
* Rank Badge System
* Platform Statistics
* Coding Analytics
* Competitive Ranking

---

### 🤖 AI Career Insights

Powered by **Groq + Llama 3**

Generates:

* Strength Analysis
* Weakness Analysis
* Career Recommendations
* Learning Roadmap
* Interview Preparation Suggestions
* Improvement Areas

---

### 🎯 AI Skill Recommendation Engine

Personalized recommendations based on:

* Coding Performance
* Platform Activity
* Developer Profile
* Problem Solving Skills

Provides:

* Recommended DSA Topics
* Suggested Projects
* Career Guidance
* Skill Gap Analysis
* Platform Improvement Plans

---

### 📄 PDF Report Generation

Generate downloadable coding reports containing:

* Developer Profile
* Total Score
* Rank Badge
* Profile Strength
* Platform Statistics
* AI Recommendations
* Career Insights

---

### 🏆 Developer Leaderboard

Track performance using:

* Score-Based Rankings
* Developer Standings
* Competitive Comparison
* Ranking System

---

### ⚖️ User Comparison System

Compare any two developers:

* Score Comparison
* Platform Analysis
* Performance Metrics
* Rank Evaluation
* Winner Detection

---

### 🗑️ Profile Management

Manage coding profiles:

* Add Profile
* Update Profile
* Search Profile
* Delete Profile

---

## 🧠 What Code Profile Analyzer Measures

* Coding Activity
* Competitive Programming Performance
* Problem Solving Skills
* GitHub Presence
* Platform Participation
* Overall Developer Strength

---

## ⚙️ Tech Stack

### Frontend

* React.js
* Vite
* Axios
* CSS3
* jsPDF

### Backend

* FastAPI
* Python
* JWT Authentication

### Database

* MongoDB Atlas
* MongoDB

### AI Layer

* Groq API
* Llama 3

---

## 🎨 UI Features

* Modern Responsive Design
* Professional Dashboard
* Profile Analytics
* Rank Badge System
* AI Insights Panel
* Profile Strength Meter
* PDF Export Interface

---

## 📁 Project Structure

```txt
Code-Profile-Analyzer/
│
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── database/
│   │   ├── models/
│   │   └── utils/
│   │
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── services/
│   │   ├── assets/
│   │   └── App.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🔍 Supported Platforms

| Platform      | Supported |
| ------------- | --------- |
| LeetCode      | ✅         |
| Codeforces    | ✅         |
| GitHub        | ✅         |
| GeeksforGeeks | ✅         |
| HackerRank    | ✅         |
| CodeChef      | ✅         |

---

## 📊 Rank Badge System

| Score Range | Badge              |
| ----------- | ------------------ |
| 0 - 699     | Beginner Coder     |
| 700 - 1499  | Intermediate Coder |
| 1500 - 2999 | Advanced Coder     |
| 3000+       | Elite Coder        |

---

## ⚡ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Ayushjssj/Code-Profile-Analyzer.git
```

---

### 2️⃣ Navigate Into Project

```bash
cd Code-Profile-Analyzer
```

---

### 3️⃣ Install Backend Dependencies

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Create `.env`

```env
MONGO_URI=YOUR_MONGO_URI

JWT_SECRET=YOUR_SECRET_KEY

GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

### 4️⃣ Install Frontend Dependencies

```bash
cd ../frontend

npm install
```

Create `.env`

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

---

## ▶️ Running The Project

### Start Backend

```bash
cd backend

uvicorn app.main:app --reload
```

Backend runs on:

```txt
http://127.0.0.1:8000
```

---

### Start Frontend

```bash
cd frontend

npm run dev
```

Frontend runs on:

```txt
http://localhost:5173
```

---

## 🌐 Main Features

| Feature               | Description                  |
| --------------------- | ---------------------------- |
| Authentication        | Login & Signup               |
| Profile Analysis      | Multi-platform analytics     |
| AI Insights           | AI-powered career guidance   |
| Skill Recommendations | Personalized AI suggestions  |
| PDF Export            | Download profile reports     |
| Leaderboard           | Competitive rankings         |
| User Comparison       | Compare developers           |
| Profile Management    | Add, update, delete profiles |

---

## 🧠 Future Improvements

* Public Shareable Profiles
* Coding Streak Tracking
* Contest Analytics
* Profile Analytics Charts
* Resume Match Score
* AI Interview Copilot Integration
* Job Recommendation Engine
* Real-Time Notifications

---

## 👨‍💻 Built By

### Ayush Pandey

🚀 GenAI Engineer
🛡️ Agentic AI Developer
💻 AI & Full Stack Developer

---

## 📜 License

This project is licensed under the MIT License.

Unauthorized copying or redistribution of this software without permission may constitute copyright infringement.

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork the project
* 🚀 Improve your coding journey

---

## 🚀 Code Profile Analyzer

#### Analyze • Compare • Rank • Recommend • Grow
