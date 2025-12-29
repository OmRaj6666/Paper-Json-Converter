from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import extract_text
from parser import parse_text
import json
import os

app = Flask(__name__)
CORS(app)  # Allow frontend requests

# Output settings
OUTPUT_DIR = "../output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "result.json")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Paper to JSON API is running"})

@app.route("/extract", methods=["POST"])
def extract():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # OCR extraction
    text = extract_text(file)

    # Parse text to JSON
    parsed_data = parse_text(text)

    # Save JSON output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(parsed_data, f, indent=2)

    return jsonify({
        "status": "success",
        "json_output": parsed_data
    })

if __name__ == "__main__":
    # ⚠️ DO NOT USE PORT 5000 ON macOS
    app.run(host="0.0.0.0", port=5001, debug=True)
