# TruthGuard AI

TruthGuard AI is a Machine Learning project built with Python and Scikit-Learn to classify news articles as **REAL** or **FAKE** based on textual content.

The project demonstrates the end-to-end Machine Learning workflow, including data preparation, text vectorization, model training, persistence, and inference.

---

## Features

- News credibility classification
- Text preprocessing and vectorization
- Machine Learning-based prediction
- Model persistence using Joblib
- Confidence score reporting
- Reusable prediction pipeline

---

## Architecture

```text
TruthGuard AI
│
├── data/
│   └── news.csv
│
├── models/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│   ├── analyzer.py
│   └── scoring.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Tech Stack

- Python 3.13
- Pandas
- Scikit-Learn
- Joblib
- Git
- GitHub

---

## Machine Learning Pipeline

### 1. Training

The model is trained using labeled news articles stored in a CSV dataset.

```bash
py src/train_model.py
```

During training, the application:

- Loads the dataset
- Converts text into numerical features using TF-IDF
- Trains a Logistic Regression model
- Saves the trained model to disk

Generated artifacts:

```text
models/fake_news_model.pkl
models/vectorizer.pkl
```

---

### 2. Prediction

Once trained, the model can classify new articles without retraining.

```bash
py src/predict.py
```

Example input:

```text
Miracle cure discovered and hidden from public.
```

Example output:

```text
Classification: FAKE

Confidence: 95.4%
```

---

## Sample Dataset

```csv
text,label
"Scientists discovered a new planet",REAL
"University releases research findings",REAL
"Secret treatment works instantly",FAKE
"Miracle cure doctors don't want you to know",FAKE
```

---

## Learning Objectives

This project was created to practice:

- Machine Learning fundamentals
- Natural Language Processing (NLP)
- Text classification
- Feature engineering
- Model persistence
- Git and GitHub workflows

---

## Future Improvements

- Larger training dataset
- Explainable AI (XAI)
- Advanced NLP preprocessing
- Model performance metrics
- Streamlit web interface
- Real-time article analysis
- Support for multiple languages

---

# TruthGuard AI

TruthGuard AI is a Machine Learning project built with Python and Scikit-Learn to classify news articles as **REAL** or **FAKE** based on textual content.

The project demonstrates a complete Machine Learning workflow including dataset ingestion, text vectorization, model training, model persistence, and content classification.

---

## Features

- Fake news detection
- Text classification using Machine Learning
- TF-IDF text vectorization
- Logistic Regression model
- Model persistence with Joblib
- Confidence score prediction
- Reusable inference pipeline

---

## Tech Stack

- Python 3.13
- Pandas
- Scikit-Learn
- Joblib
- Git
- GitHub

---

## Project Structure

```text
truthguard-ai/
│
├── data/
│   └── news.csv
│
├── models/
│   ├── fake_news_model.pkl
│   └── vectorizer.pkl
│
├── src/
│   ├── train_model.py
│   ├── predict.py
│   ├── analyzer.py
│   └── scoring.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## How It Works

### Training Phase

The model is trained using a labeled dataset containing legitimate and fake news examples.

```bash
py src/train_model.py
```

During training, the application:

1. Loads the dataset
2. Converts text into numerical features using TF-IDF
3. Trains a Logistic Regression model
4. Saves the trained model for future predictions

Generated artifacts:

```text
models/fake_news_model.pkl
models/vectorizer.pkl
```

---

### Prediction Phase

After training, the model can analyze new text without retraining.

```bash
py src/predict.py
```

Example input:

```text
Miracle cure discovered and hidden from public.
```

Example output:

```text
Classification: FAKE

Confidence: 95.4%
```

---
## Screenshots

### Most Likely Fake

most%20likely%20fake.png

### Most Likely Real

most%20likely%20real.png

## Sample Dataset

```csv
text,label
"Scientists discovered a new planet",REAL
"Researchers publish climate study",REAL
"New vaccine shows positive results",REAL
"Miracle cure doctors don't want you to know",FAKE
"Secret treatment works instantly",FAKE
```

---

## Learning Objectives

This project was developed to explore:

- Machine Learning fundamentals
- Natural Language Processing (NLP)
- Text classification
- Feature engineering
- Model persistence
- Python development
- Git and GitHub workflows

---

## Future Improvements

- Larger training datasets
- Explainable AI (XAI)
- Advanced NLP preprocessing
- Streamlit web interface
- Multi-language support
- Real-time news analysis
- Model performance metrics

---

## Author

**Thiago Farias**

Technology professional passionate about Artificial Intelligence, Machine Learning, Automation, and Data Analytics.

This project was developed as a hands-on initiative to explore NLP and Machine Learning concepts using Python.
