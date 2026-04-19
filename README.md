# 📄 AI Resume Analyzer

An AI-powered Resume Analyzer built using Python and Streamlit that helps job seekers evaluate their resumes against job descriptions and improve their chances of getting shortlisted.

---

## 🚀 Live Demo

👉 (Add your Streamlit link here after deployment)

---

## 📌 Problem Statement

Many candidates get rejected due to poor resume optimization and lack of ATS (Applicant Tracking System) compatibility.

This project solves that by:

* Comparing resumes with job descriptions
* Identifying missing keywords
* Providing a match score

---

## 💡 Features

* 📂 Upload Resume (PDF)
* 📝 Paste Job Description
* 📊 Keyword Match Score (ATS-based)
* 🤖 Semantic Similarity using TF-IDF
* ❌ Missing Keywords Detection
* ⚡ Fast and interactive UI using Streamlit

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Natural Language Processing (NLP)**
* **Scikit-learn (TF-IDF Vectorizer)**
* **PyPDF2**

---

## ⚙️ How It Works

1. Extracts text from uploaded resume
2. Cleans and preprocesses the text
3. Compares resume with job description
4. Calculates:

   * Keyword match score
   * Semantic similarity
5. Displays missing keywords and insights

---

## 📁 Project Structure

```id="s1f3kl"
ai-resume-analyzer/
│
├── app.py
├── utils/
│   ├── text_extractor.py
│   ├── preprocess.py
│   ├── matcher.py
│
├── models/
│   ├── tfidf_model.py
│
├── requirements.txt
└── README.md
```

---

## 🖥️ Installation & Setup

```bash id="3n2lks"
# Clone the repository
git clone https://github.com/javvajibhuvi24/ai-resume-analyzer.git

# Navigate to the project directory
cd ai-resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

## 📊 Example Output

* Keyword Match Score: 75%
* Semantic Similarity: 82%
* Missing Keywords: Python, Machine Learning, SQL

---

## 🔮 Future Enhancements

* AI-based resume suggestions (like ChatGPT feedback)
* Section-wise analysis (Skills, Experience)
* Resume score breakdown
* Job recommendation system
* Integration with job platforms

---

## 🎯 Learning Outcomes

* Practical implementation of NLP concepts
* Understanding of ATS-based resume filtering
* Building end-to-end AI applications
* Deploying real-world projects

---

## 👨‍💻 Author

**Bhuvi Javvaji**

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---
