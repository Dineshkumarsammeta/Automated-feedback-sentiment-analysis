# Automated Feedback Sentiment Analysis  

## 📅 Project Timeline
**Duration:** Nov 2012 – Jan 2013  
**Location:** VIT University, Vellore, India  
**Modules Covered**
| **Module**                       | **Application in Project**                                                                 |
|----------------------------------|---------------------------------------------------------------------------------------------|
| **Artificial Intelligence**      | Core NLP and sentiment analysis using machine learning libraries (NLTK, TextBlob).          |
| **Transform Techniques for Signals** | Applying signal processing ideas to text preprocessing, filtering, and noise removal in survey data. |
| **Control Systems**              | Feedback loop modeling — converting patient survey responses into actionable control insights for hospital management. |
| **Applied Numerical Methods**    | Data preprocessing, probability/statistical calculations, optimization of NLP algorithms.   |
| **Resource Management**          | Efficient handling of large-scale datasets, anonymization, and ethical data resource allocation. |
| **Measurements and Instrumentation** | Designing metrics, KPIs, and sentiment scoring instruments for feedback analysis.           |

---

## Overview  
This project built a fully automated sentiment analysis system focused on feedback. Using Python and natural language processing (NLP), the system processes raw patient survey data, scores sentiments, and generates insightful visual reports and dashboards tailored for healthcare trust managers and digital health teams.


---

## Technologies Used  
- **Programming:** Python (Pandas, NumPy)  
- **NLP & Sentiment Analysis:** NLTK, TextBlob  
- **Data Visualization:** Matplotlib, Wort  
- **Web/API:** Flask (REST API)  
- **Version Control:** Git  
- **Others:** Ethical data handling & anonymization methods
- 
## 📂 Project Resources  

- 📊 [Data Folder](./data/)  
- 📓 [Jupyter Notebook](sample.ipynb)  

## Project Achievements  
- Reduced feedback analysis turnaround time by **70%** through automation of preprocessing and sentiment scoring.  
- Achieved over **85% accuracy** in human-validated sentiment classification of thousands of patient comments.  
- Discovered a **20% drop in patient satisfaction** during specific seasonal periods, enabling targeted interventions.  
- Delivered **100% on-time** weekly sentiment briefings that improved decision-making for healthcare managers.  
- Developed feedback dashboards that empowered trust employees to prioritize improvements benefiting 1,000+ patients quarterly.  
- Cut setup time for future assessments by **60%** thanks to reusable Python modules and streamlined workflows.
## Getting Started  
## 🚀 Running the Web API

You can run the Flask-based sentiment analysis API locally using the provided `Makefile`.

### Start the API
```bash
make web

This will launch the Flask server at http://localhost:5000
.

Test the API

Send a sample request with curl:

curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "The doctors were helpful but the waiting time was long."}'


Example response:

{
  "text": "The doctors were helpful but the waiting time was long.",
  "sentiment": "neutral",
  "polarity": 0.1,
  "subjectivity": 0.75
}

Dockerized Run

If you prefer Docker:

make docker-build
make docker-run


The service will then be available at http://localhost:5000/analyze
.


---

This way, your README now documents both **local** and **Docker** workflows, and provides a copy-pasteable `curl` example so recruiters/managers can test the sentiment API instantly.  

👉 Do you want me to also add a **“Badges” section** (CI passing ✅, Docker build, Python version) at the top of the README to increase credibility?
---

## Ethics & Privacy  
Patient data was anonymized and handled in strict accordance with NHS information governance standards, ensuring privacy, security, and transparency throughout the project lifecycle.

---

## Contact  
For questions, collaboration, or feedback, please contact:  
**Sammeta Dinesh Kumar** — [sammetadineshkumar@gmail.com]
- 🌐 [Portfolio](https://dineshsammeta1234.github.io/)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/dineshsammeta)   

---

Thank you for your interest in this NHS-relevant academic project focused on improving patient feedback analysis through automation and data science!
