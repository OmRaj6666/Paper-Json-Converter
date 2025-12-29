📌 Overview
The Paper-to-JSON Converter is a lightweight document digitization system that converts scanned paper documents into structured JSON format.
It leverages OCR (Optical Character Recognition) for text extraction and a rule-based parsing pipeline to generate machine-readable data.

🎯 Problem Statement

Paper-based documents are:
Difficult to search
Hard to integrate with digital systems
Prone to redundancy and data loss
This project addresses these challenges by converting physical documents into structured JSON data.

✅ Solution Approach

Upload scanned document
Extract text using OCR
Parse key fields
Generate structured JSON
Persist output for reuse
🧩 Key Features
📤 Document upload interface
🔍 OCR-based text extraction
🧠 Rule-based parsing
📦 JSON generation
💾 Output persistence
🌐 RESTful API
⚙️ macOS-safe port configuration
🛠️ Technology Stack
Backend
Python 3.9+
Flask
Tesseract OCR
Pillow
Flask-CORS
Frontend
HTML5
CSS3
JavaScript (Fetch API)

🏗️ System Architecture
Architecture Type: Client–Server (REST-based)
User → Frontend → Flask API → OCR Engine → Parser → JSON Output

🖼️ Architecture Diagram

The following diagram illustrates the high-level architecture and data flow of the system.
📌 System Architecture Screenshot

📍 How to add this screenshot:
Render architecture.puml using PlantUML


📂 Project Structure
PAPER-TO-JSON/
│
├── backend/
│   ├── app.py
│   ├── ocr.py
│   ├── parser.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── output/
│   └── result.json
│
└── docs/
    └── architecture.png

🔁 Data Flow
User uploads scanned document
Frontend sends file to backend
OCR extracts raw text
Parser structures data
JSON is returned and stored

▶️ Installation & Setup
Prerequisites
Python 3.9+
Tesseract OCR installed and added to PATH
Install Dependencies
cd backend
pip install -r requirements.txt
Run Backend
python app.py
Server runs at:
http://127.0.0.1:5001
Run Frontend
Open frontend/index.html using Live Server
🧪 Sample Input
Name: Om Raj
Roll No: 21BCE1234
Department: CSE
College: VIT Bhopal University

📦 Sample Output (JSON)
{
  "name": "Om Raj",
  "roll_no": "21BCE1234",
  "department": "CSE",
  "college": "VIT Bhopal University"
}


🔒 Error Handling & Reliability
Missing file validation
Safe CORS configuration
Graceful API error handling
macOS port conflict avoidance

🚀 Future Enhancements
PDF support
AI/LLM-based smart extraction
Confidence scoring
Database integration
Cloud deployment
Authentication & authorization

🎓 Academic & Professional Relevance
This project demonstrates:
OCR integration
REST API design
Data digitization pipelines
Client–server architecture
Practical automation use cases