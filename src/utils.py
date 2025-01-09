import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
import joblib
import pandas as pd

def preprocess_and_train(data_path, model_path):
    # Load the dataset
    with open(data_path, 'r') as file:
        data = json.load(file)

    # Extract questions and answers
    questions = [item['question'] for item in data['questions']]
    intents = range(len(data['questions']))  # Assign a unique ID for each question

    # Create a DataFrame
    df = pd.DataFrame({'Question': questions, 'Intent': intents})

    # Create a pipeline with TF-IDF Vectorizer and Logistic Regression
    pipeline = make_pipeline(
        TfidfVectorizer(),
        LogisticRegression()
    )

    # Train the model
    pipeline.fit(df['Question'], df['Intent'])

    # Save the trained model
    joblib.dump((pipeline, data['questions']), model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    preprocess_and_train("data/Ecommerce_FAQ_Chatbot_dataset.json", "src/intent_model.pkl")
