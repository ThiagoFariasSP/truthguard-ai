import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("data/news.csv")

# Convert text into numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(df["text"])

# Labels
y = df["label"]

# Train model
model = LogisticRegression()

model.fit(X, y)
joblib.dump(model, "models/fake_news_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("Model saved successfully!")
print("Model trained successfully!")

# Test prediction
sample = ["Miracle cure discovered and hidden from public"]

sample_vector = vectorizer.transform(sample)

prediction = model.predict(sample_vector)

print("Prediction:", prediction[0])