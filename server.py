
from flask import Flask, jsonify, request, send_from_directory
from pathlib import Path
from datetime import datetime
import json

from main import VOCABULARY, DATA_FILE, load_progress

app = Flask(__name__, static_folder=None)
BASE_DIR = Path(__file__).resolve().parent


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<path:filename>")
def website_files(filename):
    allowed_files = {
        "about.html",
        "services.html",
        "contact.html",
        "style.css",
        "script.js",
    }

    if filename not in allowed_files:
        return jsonify({"error": "File not found"}), 404

    return send_from_directory(BASE_DIR, filename)


@app.route("/api/vocabulary")
def get_vocabulary():
    return jsonify(VOCABULARY)


@app.route("/api/progress")
def get_progress():
    try:
        progress = load_progress()
        return jsonify(progress)
    except Exception:
        app.logger.exception("Could not read progress")
        return jsonify({"error": "Could not read progress"}), 500


@app.route("/api/quiz-result", methods=["POST"])
def save_quiz_result():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid request data"}), 400

    score = data.get("score")
    total = data.get("total")

    # Reject invalid values, including booleans.
    if (
        type(score) is not int
        or type(total) is not int
        or total <= 0
        or score < 0
        or score > total
    ):
        return jsonify({"error": "Invalid score or total"}), 400

    try:
        progress = load_progress()

        progress["quizzes"] = int(progress.get("quizzes", 0)) + 1
        progress["correct"] = int(progress.get("correct", 0)) + score
        progress["answered"] = int(progress.get("answered", 0)) + total

        history = progress.get("quiz_history", [])
        if not isinstance(history, list):
            history = []

        history.append({
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "type": "Web Vocabulary",
            "score": score,
            "total": total,
            "percentage": round(score / total * 100),
        })

        progress["quiz_history"] = history[-50:]

        DATA_FILE.write_text(
            json.dumps(progress, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        return jsonify({
            "success": True,
            "message": "Quiz result saved successfully",
        })

    except (OSError, ValueError, TypeError):
        app.logger.exception("Could not save quiz result")
        return jsonify({"error": "Could not save quiz result"}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
