# AI Resume Analyzer 🚀

## 📌 Project Overview

AI Resume Analyzer is a full-stack web application that analyzes resumes and provides insights such as ATS score, skill extraction, match score, and improvement suggestions.
The system uses a combination of **React (frontend)**, **Node.js (backend)**, and **Python (ML processing)**.

---

## 🏗️ Tech Stack

**Frontend**

* React.js
* Axios
* CSS (Custom UI)

**Backend**

* Node.js
* Express.js

**Machine Learning**

* Python
* Flask
* NLP (basic skill extraction logic)

---

## ⚙️ Features

* 📄 Upload resume (PDF)
* 🎯 ATS Score calculation
* 📊 Match Score analysis
* 🛠 Skill extraction
* 💡 Suggestions for improvement
* 🌙 Dark/Light mode toggle
* 📥 Download report as PDF

---

## 📁 Project Structure

```
ai/
│
├── backend/
│   ├── server.js
│   └── package.json
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   └── package.json
│
├── ml_model/
│   ├── app.py
│   ├── resume_extract.py
│   ├── skill_analyzer.py
│   └── job_match.py
│
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```
git clone <your-repo-link>
cd ai
```

---

### 2️⃣ Run ML Model (Python)

```
cd ml_model
pip install flask pandas scikit-learn
python app.py
```

Runs on:

```
http://127.0.0.1:5000
```

---

### 3️⃣ Run Backend (Node.js)

```
cd backend
npm install
node server.js
```

Runs on:

```
http://localhost:3001
```

---

### 4️⃣ Run Frontend (React)

```
cd frontend
npm install
npm start
```

Runs on:

```
http://localhost:3000
```

---

## 🔄 Application Flow

```
React (Frontend)
        ↓
Node.js (Backend)
        ↓
Python ML Model
        ↓
Response to Frontend
```

---

## 📊 Sample Output

* ATS Score: 75%
* Match Score: 68%
* Skills: Python, JavaScript, React
* Suggestions:

  * Add more project experience
  * Include measurable achievements
  * Improve keyword matching

---

## ⚠️ Notes

* Ensure all three servers (Frontend, Backend, ML) are running simultaneously.
* Python API must be running before backend requests.
* Update API URLs if ports are changed.

---

## 🔮 Future Enhancements

* Real NLP-based resume parsing
* Job description matching
* Keyword highlighting in resume
* User authentication system
* Database integration

---

## 👩‍💻 Author

Anushka Goswami
B.Tech Student | Full Stack Developer | DSA Enthusiast

---

## 📄 License

This project is for educational and portfolio purposes.
