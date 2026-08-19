import joblib

# Load trained assets
model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

print("=== TruthGuard AI ===")

text = input("\nPaste article text:\n\n")

text_vector = vectorizer.transform([text])

prediction = model.predict(text_vector)[0]

probability = model.predict_proba(text_vector).max() * 100

print("\nResult")
print("-" * 30)
print(f"Classification: {prediction}")
print(f"Confidence: {probability:.2f}%")