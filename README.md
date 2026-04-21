# 🚀 HR Recruitment Management System
---

## 📌 Overview

This project is an **automated HR recruitment system** that helps recruiters efficiently screen and rank candidates based on job descriptions.

It uses **Natural Language Processing (NLP)** techniques to extract skills from resumes and match them with job requirements using **TF-IDF and Cosine Similarity**.

---

## 🎯 Key Features

* ✅ Resume Data Ingestion (CSV-based)
* ✅ Data Cleaning & Preprocessing
* ✅ Automatic Skill Extraction (NLP)
* ✅ MySQL Database Integration
* ✅ Resume Matching using TF-IDF
* ✅ Candidate Ranking System (Top 3 Results)
* ✅ Modular & Scalable Architecture

---

## 🧠 How It Works

1. Load resume data from CSV
2. Clean and preprocess data
3. Extract skills from resume text
4. Store processed data in MySQL
5. Input job description
6. Convert text into vectors (TF-IDF)
7. Compute similarity (Cosine Similarity)
8. Rank candidates and return top matches

---

## 🏗️ Project Structure

```
hr_resume_system/
│
├── config/
├── data/
│   ├── raw/
│   └── processed/
│
├── modules/
├── scripts/
├── logs/
├── run_pipeline.sh
└── README.md
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** MySQL
* **Libraries:** Pandas, Scikit-learn
* **NLP:** TF-IDF, Regex
* **Environment:** Virtual Environment (venv)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/hr-resume-system.git
cd hr-resume-system
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv mven
mven\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install pandas mysql-connector-python scikit-learn
```

---

### 4️⃣ Setup MySQL Database

```sql
CREATE DATABASE hr_system;
```

Update your credentials in:

```
config/config.py
```

---

## ▶️ Run the Project

### Step 1: Data Cleaning

```bash
python -m scripts.clean
```

---

### Step 2: Load Data into MySQL

```bash
python -m scripts.load_mysql
```

---

### Step 3: Run Matching System

```bash
python -m scripts.match
```

---

## 🧪 Example

**Input:**

```
Python developer with SQL and machine learning
```

**Output:**

```
Top 3 Candidates:
Santanu   0.91
Anita     0.76
Rahul     0.30
```

---

## 🌟 Key Highlights

* 🔹 Combines **Data Engineering + Machine Learning**
* 🔹 Real-world **HR Applicant Tracking System (ATS)**
* 🔹 Automated resume screening & ranking
* 🔹 Clean and modular project structure

---

## ⚠️ Limitations

* Keyword-based skill extraction
* Limited understanding of synonyms (e.g., ML vs Machine Learning)

---

## 🚀 Future Improvements

* 🔹 Resume PDF parsing
* 🔹 BERT-based semantic matching
* 🔹 Skill synonym detection
* 🔹 Web dashboard (Flask/React)
* 🔹 Cloud deployment (AWS/GCP)

---

## 👨‍💻 Author

**Santanu Maity**
B.Tech CSE | KIIT University

---

## 📜 License

This project is for educational purposes.

---
