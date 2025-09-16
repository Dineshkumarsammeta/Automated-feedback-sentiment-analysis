from flask import request, jsonify
from .analysis import analyze_text

def register_routes(app):
    @app.route("/", methods=["GET"])
    def index():
        return jsonify({"message": "Automated Feedback Sentiment Analysis API"})

    @app.route("/analyze", methods=["POST"])
    def analyze():
        """
        Example: curl -X POST http://localhost:5000/analyze \
            -H "Content-Type: application/json" \
            -d '{"text": "The doctors were very helpful but the waiting time was long."}'
        """
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        result = analyze_text(data["text"])
        return jsonify(result)
