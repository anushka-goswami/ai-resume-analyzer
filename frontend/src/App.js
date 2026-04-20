import React, { useState } from "react";
import axios from "axios";
import jsPDF from "jspdf";
import "./App.css";

function App() {

  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [darkMode, setDarkMode] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a resume file");

    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/analyze", formData);
      setResult(res.data);
    } catch (err) {
      alert("Backend error");
    }

    setLoading(false);
  };

  // 🎯 Resume Grade Logic
  const getGrade = (score) => {
    if (score >= 80) return "A";
    if (score >= 60) return "B";
    return "C";
  };


  const downloadPDF = () => {
    const doc = new jsPDF();
    doc.text("Resume Analysis Report", 20, 20);
    doc.text(`ATS Score: ${result.ats_score}%`, 20, 40);
    doc.text(`Match Score: ${result.match_score}%`, 20, 50);

    doc.text("Skills:", 20, 65);
    result.skills.forEach((skill, i) => {
      doc.text(`- ${skill}`, 25, 75 + (i * 8));
    });

    doc.save("resume-report.pdf");
  };

  return (
    <div className={darkMode ? "container dark" : "container"}>

      <div className="top-bar">
        <h2>AI Resume Analyzer 🚀</h2>
        <button
          className="toggle-btn"
          onClick={() => setDarkMode(!darkMode)}
        >
          {darkMode ? "Light Mode ☀" : "Dark Mode 🌙"}
        </button>
      </div>

      <div className="upload-section">
        <input type="file" accept=".pdf" onChange={handleFileChange} />
        <button className="button" onClick={handleUpload}>
          {loading ? "Analyzing..." : "Analyze Resume"}
        </button>
      </div>

      {result && (
        <div className="results">

          {/* 🎯 Circular Score */}
          <div className="score-section">
            <div className="circle">
              <svg>
                <circle cx="70" cy="70" r="60"></circle>
                <circle
                  cx="70"
                  cy="70"
                  r="60"
                  style={{
                    strokeDashoffset:
                      377 - (377 * result.ats_score) / 100
                  }}
                ></circle>
              </svg>
              <div className="score-text">
                {result.ats_score}%
              </div>
            </div>

            <div className={`grade grade-${getGrade(result.ats_score)}`}>
              Grade {getGrade(result.ats_score)}
            </div>
          </div>

          <p><strong>Match Score:</strong> {result.match_score}%</p>

          <h4>Skills 🛠</h4>
          <div className="skills">
            {result.skills.map((skill, i) => (
              <span key={i} className="skill-tag">
                {skill}
              </span>
            ))}
          </div>

          <h4>Suggestions 💡</h4>
          <ul>
            {result.suggestions.map((s, i) => (
              <li key={i}>{s}</li>
            ))}
          </ul>

          <button className="button download" onClick={downloadPDF}>
            Download PDF Report 📄
          </button>

        </div>
      )}

    </div>
  );
}

export default App;