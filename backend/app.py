from flask import Flask, jsonify
import random
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

QUOTES = [
    "The secret of getting ahead is getting started. — Mark Twain",
    "Do not wait to strike till the iron is hot; but make it hot by striking. — W.B. Yeats",
    "The future depends on what you do today. — Mahatma Gandhi",
    "It always seems impossible until it's done. — Nelson Mandela",
    "You miss 100% of the shots you don't take. — Wayne Gretzky",
    "Action is the foundational key to all success. — Pablo Picasso",
    "Don't watch the clock; do what it does. Keep going. — Sam Levenson"
]

REQUEST_COUNT = Counter("quote_requests_total", "Total number of quote requests")

@app.route("/")
def home():
    return jsonify({"message": "Quote Generator API is running 🚀"}), 200

@app.route("/quote")
def quote():
    REQUEST_COUNT.inc()
    return jsonify({"quote": random.choice(QUOTES)}), 200

@app.route("/metrics")
def metrics():
    data = generate_latest()
    return (data, 200, {"Content-Type": CONTENT_TYPE_LATEST})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
