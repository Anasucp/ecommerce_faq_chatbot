from flask import Flask, request, jsonify, render_template
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the trained model and dataset
model, questions_data = joblib.load("src/intent_model.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Get the user's question
    user_input = request.json.get("question")

    # Predict the intent ID
    intent_id = model.predict([user_input])[0]

    # Retrieve the response based on the predicted intent ID
    response = questions_data[int(intent_id)]['answer']
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
