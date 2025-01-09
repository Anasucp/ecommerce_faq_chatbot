# **eCommerce FAQ Chatbot**

An AI-powered chatbot built using Flask and Machine Learning that answers frequently asked questions (FAQs) about an eCommerce platform. This chatbot uses a trained model to classify user questions and respond with relevant answers.

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Requirements](#requirements)
5. [Setup and Installation](#setup-and-installation)
6. [Directory Structure](#directory-structure)
7. [How to Run Locally](#how-to-run-locally)
8. [Deployment on Railway](#deployment-on-railway)
9. [Screenshots](#screenshots)
10. [Challenges and Limitations](#challenges-and-limitations)
11. [Future Considerations](#future-considerations)

---

## **Introduction**
This chatbot provides instant responses to users' common queries about an eCommerce platform, such as tracking orders, return policies, account creation, and more. The application uses a pre-trained intent classification model and Flask for backend functionality, ensuring fast and accurate responses.

### **Why it’s significant?**
- Saves customer support time by automating repetitive tasks.
- Enhances user experience with real-time, personalized assistance.
- Easy to integrate into existing eCommerce platforms.

---

## **Features**
- **Interactive Chat Interface**: Users can type their questions and receive instant responses in a chat-style UI.
- **Suggested Questions**: A set of clickable, common questions to assist users quickly.
- **Modern UI**: Includes animations, a dark mode-inspired theme, and a sleek layout.
- **Typing Indicator**: Simulates a "typing..." effect for a realistic experience.
- **Scalable**: Easy to train and deploy with additional data.

---

## **Dataset**
The chatbot uses the **Ecommerce_FAQ_Chatbot_dataset.json** file, which contains a structured set of questions and answers related to eCommerce scenarios. Example:

```json
{
  "questions": [
    {
      "question": "How can I create an account?",
      "answer": "To create an account, click on the 'Sign Up' button on the top right corner of our website and follow the instructions to complete the registration process."
    },
    {
      "question": "What is your return policy?",
      "answer": "Our return policy allows you to return products within 30 days of purchase for a full refund, provided they are in their original condition and packaging."
    }
  ]
}
```

---

## **Requirements**
The project requires the following dependencies:
- **Flask**: For building the chatbot backend.
- **scikit-learn**: For training and using the intent classification model.
- **joblib**: For saving and loading the trained model.
- **pandas**: For data manipulation.

Install all dependencies using the command:
```bash
pip install -r requirements.txt
```

---

## **Setup and Installation**

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/USERNAME/REPOSITORY_NAME.git
cd ecommerce_faq_chatbot
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Train the Model**
Run the following command to train the chatbot's intent classification model:
```bash
python3 src/utils.py
```

This script will:
1. Load the dataset (`Ecommerce_FAQ_Chatbot_dataset.json`).
2. Train a machine learning model using Logistic Regression.
3. Save the model to `src/intent_model.pkl`.

---

## **Directory Structure**
```
ecommerce_faq_chatbot/
├── data/
│   └── Ecommerce_FAQ_Chatbot_dataset.json      # Dataset with questions and answers
├── src/
│   ├── app.py                                 # Flask application for backend
│   ├── utils.py                               # Preprocessing and training script
│   ├── intent_model.pkl                       # Trained intent classification model
│   └── templates/
│       └── index.html                         # Frontend HTML file
├── requirements.txt                           # Dependencies
├── Procfile                                   # For deployment on Railway
├── README.md                                  # Project instructions
```

---

## **How to Run Locally**
1. **Start the Flask Application**
   ```bash
   python3 src/app.py
   ```

2. **Access the Chatbot**
   Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Deployment on Railway**
1. Push your project to GitHub:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
   git push -u origin main
   ```

2. Deploy on [Railway](https://railway.app/):
   - Sign in to Railway with GitHub.
   - Create a new project and link your repository.
   - Add environment variables if needed.
   - Deploy and get your live URL!

---

## **Challenges and Limitations**
- **Limited Dataset**: The chatbot's responses are restricted to the dataset provided. Expanding the dataset can improve its capabilities.
- **Language Barrier**: The chatbot currently supports only English. Multi-language support can be implemented in the future.
- **No Context Awareness**: The chatbot does not retain conversational context across multiple questions.
