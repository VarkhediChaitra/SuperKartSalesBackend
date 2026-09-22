from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load the model outside the request handler to avoid reloading it on every request
# This assumes model_filename and backend_sources are defined elsewhere or passed in.

model_filename = "forecast_superkart_sales_model.joblib"
current_dir = os.path.dirname(__file__)   # auto-resolves to /app/backend_sources
saved_model = joblib.load(os.path.join(current_dir, model_filename))

# --- Single prediction endpoint ---
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        # Convert input dict to DataFrame (1 row)
        df = pd.DataFrame([data])

        # Run prediction
        prediction = saved_model.predict(df)[0]

        return jsonify({"Sales": float(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# --- Batch prediction endpoint ---
@app.route("/batch_predict", methods=["POST"])
def batch_predict():
    try:
        data_list = request.get_json(force=True)

        # Expecting a list of dicts
        if not isinstance(data_list, list):
            return jsonify({"error": "Input must be a list of records"}), 400

        df = pd.DataFrame(data_list)
        predictions = saved_model.predict(df)

        # Return predictions alongside input
        results = [
            {"input": record, "Sales": float(pred)}
            for record, pred in zip(data_list, predictions)
        ]

        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # This block is typically for local development, not for Gunicorn deployment
    app.run(host='0.0.0.0', port=7860, debug=True)
