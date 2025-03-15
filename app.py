from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(name)

# Load the model (directly using the pre-trained model)
model = pipeline("text-generation", model="gpt2")  # You can change 'gpt2' to other models if needed.

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")
    
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = model(prompt, max_length=100, num_return_sequences=1)
        return jsonify({"generated_text": response[0]["generated_text"]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if name == "main":
    app.run(host='0.0.0.0', port=5000)