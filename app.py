import streamlit as st
import pickle

#Page configure
st.set_pagec
# Load saved model and vectorizer
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Student Feedback Sentiment Classifier")

st.write("Enter your feedback below to predict sentiment.")

# User input
user_input = st.text_area("Type your feedback here:")

if st.button("Predict"):
    if user_input.strip() != "":
        # Convert text to vector
        input_vector = vectorizer.transform([user_input])
        
        # Predict
        prediction = model.predict(input_vector)[0]
        
        st.success(f"Predicted Sentiment: {prediction}")
    else:
        st.warning("Please enter some text.")