# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using Machine Learning and Natural Language Processing techniques.

The application recommends movies similar to a selected movie by analyzing genres, keywords, and movie overviews using TF-IDF Vectorization and Cosine Similarity.

The project also integrates the OMDb API to fetch movie posters and plot summaries, providing an interactive user experience through a Streamlit web application.

---

## 🚀 Features

* Content-Based Movie Recommendation
* TF-IDF Vectorization
* Cosine Similarity Matching
* Interactive Streamlit Web Interface
* Movie Posters using OMDb API
* Movie Plot Summaries
* Fast Recommendation Generation
* Responsive UI with Movie Cards

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning & NLP

* Scikit-Learn
* NLTK
* TF-IDF Vectorizer
* Cosine Similarity

### Web Interface

* Streamlit

### Data Processing

* Pandas
* NumPy

### External API

* OMDb API

---

## 📷 Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Recommendations

![Recommendations](screenshots/recommendations.png)

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone <your-repository-url>
cd movie_recommendation
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 OMDb API Setup

1. Visit https://www.omdbapi.com/apikey.aspx
2. Generate a free API key.
3. Create a file named `config.json`.

Example:

```json
{
    "OMDB_API_KEY": "YOUR_API_KEY"
}
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 🧠 Machine Learning Workflow

1. Load movie dataset
2. Clean and preprocess text
3. Combine genres, keywords, and overview
4. Apply TF-IDF Vectorization
5. Compute Cosine Similarity Matrix
6. Recommend most similar movies

---

## 📌 Future Improvements

* Hybrid Recommendation System
* Genre Filtering
* Movie Ratings Integration
* User Authentication
* Deployment on Streamlit Cloud

---

## 👨‍💻 Author

Dharya Thakkar
