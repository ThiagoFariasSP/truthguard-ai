import joblib
import streamlit as st

model = joblib.load("models/fake_news_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.title("TruthGuard AI")

text = st.text_area("Paste a news article:")

if st.button("Analyze"):

    if text.strip():

        vector = vectorizer.transform([text])

        prediction = model.predict(vector)[0]

        confidence = model.predict_proba(vector).max() * 100

        if prediction == "FAKE":
            st.error("Most Likely Fake")
        else:
            st.success("Most Likely Real")

        st.info(f"Confidence: {confidence:.2f}%")

    else:
        st.warning("Please enter some text.")