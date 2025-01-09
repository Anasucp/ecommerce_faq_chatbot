from flask import Flask, request, jsonify, render_template
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and dataset
model, questions_data = joblib.load("src/intent_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's question from the POST request body
    user_input = request.json.get("question")
    
    # Predict the intent ID using the trained model
    intent_id = model.predict([user_input])[0]

    # Retrieve the corresponding response from the questions data
    response = questions_data[int(intent_id)]['answer']
    
    # Return the response in JSON format
    return jsonify({"response": response})

# Ensure the Flask app runs on the correct host and port for deployment
if __name__ == "__main__":
    # Use the environment variable PORT provided by Railway (default to 5000 if not set)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)  # Disable debug mode for production

