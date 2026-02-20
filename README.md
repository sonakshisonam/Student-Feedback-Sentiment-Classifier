# Student-Feedback-Sentiment-Classifier
A simple Machine Learning project that predicts sentiment (Positive, Negative, Neutral) from student feedback text using Python and Streamlit.

---

## 📌 About the Project

This project is based on a simple idea:

Students give feedback about apps, classes, or services.  
It is useful to automatically understand whether the feedback is Positive, Negative, or Neutral.

So, I built a Machine Learning model that:
- Takes text input
- Converts text into numerical form using TF-IDF
- Uses Logistic Regression for classification
- Displays prediction through a Streamlit web app

---

## 🛠 Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Pickle

---

## ⚙ Project Workflow

1. Load dataset
2. Text preprocessing
3. Convert text to vectors (TF-IDF)
4. Split into training and testing data
5. Train Logistic Regression model
6. Evaluate using Accuracy & Confusion Matrix
7. Save model using Pickle
8. Deploy using Streamlit

---

## ✨ Features

- Real-time sentiment prediction
- Simple and clean UI
- Trained ML model
- Easy to deploy
- Supports Positive / Negative / Neutral classification

---

## 🚀 How to Run the Project

Follow these steps to run the project on your system:

### Step 1: Clone the Repository

```
git clone https://github.com/sonakshisonam/Student-Feedback-Sentiment-Classifier.git
cd Student-Feedback-Sentiment-Classifier
```
Install Python then- 
pip install -r requirements.txt

Run Streamlit App 
streamlit run app.py
