import os
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Load trained model and vectorizer ---
def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_dir, "models", "count_vectorizer.pkl"), "rb") as f:
        vectorizer = pickle.load(f)
    with open(os.path.join(base_dir, "models", "basic_classifier.pkl"), "rb") as f:
        clf = pickle.load(f)
    return vectorizer, clf

# Load once on startup
VECT, CLF = load_model()

@app.route('/')
def home():
    return jsonify({"status": "ok"}), 200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        text = data.get('text', '')

        if not isinstance(text, str) or not text.strip():
            return jsonify({"error": "Invalid or empty text"}), 400

        X = VECT.transform([text])
        prediction = CLF.predict(X)[0]

        return jsonify({"prediction": str(prediction)})

    except Exception as e:
        import traceback
        error_message = traceback.format_exc()
        print("PREDICTION ERROR:", error_message, flush=True)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
